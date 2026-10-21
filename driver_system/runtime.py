import hashlib,json
from pathlib import Path
import cv2
import numpy as np
import torch
from torch import nn
from .gaze_runtime import Encoder,GazePredictor
from .preprocess import PairPreprocessor,letterbox
from .policy import TemporalPolicy,signals_from_predictions
from .window_policy import WindowPolicy,binary_signals
from .action_policy import ActionHysteresis,merge_action_alerts

class MultiHead(nn.Module):
    def __init__(self,classes):
        super().__init__();self.backbone=Encoder()
        self.heads=nn.ModuleDict({h:nn.Sequential(nn.Dropout(.2),nn.Linear(512,len(c))) for h,c in classes.items()})
    def forward(self,x):
        z=self.backbone(x);return {h:v(z) for h,v in self.heads.items()}

class Predictor:
    def __init__(self,path,entry,device):
        if hashlib.sha256(path.read_bytes()).hexdigest()!=entry['sha256']:raise ValueError('Checkpoint hash mismatch')
        ck=torch.load(path,map_location='cpu',weights_only=True)
        if ck['config']['classes']!=entry['classes']:raise ValueError('Class order mismatch')
        self.classes=entry['classes'];self.device=device;self.model=MultiHead(self.classes)
        self.model.load_state_dict(ck['state_dict'],strict=True);self.model.to(device).eval()
    @torch.inference_mode()
    def predict(self,rgb):
        a=rgb.astype(np.float32)/255
        a=(a-np.array([.485,.456,.406],np.float32))/np.array([.229,.224,.225],np.float32)
        x=torch.from_numpy(a.transpose(2,0,1).copy())[None].to(self.device)
        result={}
        for h,p in self.model(x).items():
            p=p.softmax(1)[0].cpu().numpy();i=int(p.argmax());classes=self.classes[h]
            result[h]={'label':classes[i],'score':float(p[i]),'probabilities':dict(zip(classes,map(float,p)))}
        return result

class DriverSystem:
    def __init__(self,bundle,device='cpu',body_visible=False,policy_config=None):
        root=Path(bundle);self.manifest=json.loads((root/'manifest.json').read_text())
        for entry in self.manifest['models'].values():
            if hashlib.sha256((root/entry['file']).read_bytes()).hexdigest()!=entry['sha256']:raise ValueError('Bundle integrity failed')
        m=self.manifest['models'];self.gaze=GazePredictor(root/m['gaze']['file'],device)
        self.drowsiness=Predictor(root/m['drowsiness']['file'],m['drowsiness'],device)
        self.action=Predictor(root/m['distraction']['file'],m['distraction'],device)
        self.preprocess=PairPreprocessor(root/'face_landmarker.task')
        self.window_config=policy_config
        if policy_config is not None:
            if policy_config.get('version') not in ('window-policy-v2','hybrid-policy-v3') or policy_config.get('models')!=self.manifest['models']:
                raise ValueError('Policy/model identity mismatch')
            self.manifest['policy']=policy_config
        self.policy=WindowPolicy(policy_config) if policy_config else TemporalPolicy(self.manifest['policy'])
        self.action_temporal=ActionHysteresis(policy_config['action_hysteresis']) if policy_config and policy_config.get('version')=='hybrid-policy-v3' else None
        self.body_visible=body_visible
    def process(self,rgb,timestamp,branches=None):
        branches=set(branches or ['gaze','eyes','yawn','action'])
        if not branches<={'gaze','eyes','yawn','action'}:raise ValueError('Unknown branch')
        predictions={};quality={'face_available':False,'eye_available':False}
        if branches & {'gaze','eyes','yawn'}:pair,quality=self.preprocess.process(rgb)
        if quality['face_available']:
            if branches & {'eyes','yawn'}:
                predictions.update({h:p for h,p in self.drowsiness.predict(pair[:,:224]).items() if h in branches})
            if 'gaze' in branches and quality['eye_available']:predictions['gaze']=self.gaze.predict(pair)
        quality['body_view_declared']=self.body_visible
        if self.body_visible and 'action' in branches:
            # Match the body training input: full frame, letterbox, JPEG90 decode.
            bgr=letterbox(cv2.cvtColor(rgb,cv2.COLOR_RGB2BGR),224)
            ok,jpg=cv2.imencode('.jpg',bgr,[cv2.IMWRITE_JPEG_QUALITY,90])
            if not ok:raise ValueError('JPEG encode failed')
            body=cv2.cvtColor(cv2.imdecode(jpg,cv2.IMREAD_COLOR),cv2.COLOR_BGR2RGB)
            predictions.update(self.action.predict(body))
        signals=binary_signals(predictions,self.window_config) if self.window_config else signals_from_predictions(predictions,self.policy.config['min_score'])
        alerts=self.policy.update(timestamp,signals)
        if self.action_temporal:
            state=self.action_temporal.update(timestamp,predictions.get('action'))
            alerts=merge_action_alerts(alerts,state);signals['distracted_action']=state['signal']
        return {'timestamp_s':timestamp,'quality':quality,'predictions':predictions,'signals':signals,
                'alerts':alerts}
    def close(self):self.preprocess.close()
