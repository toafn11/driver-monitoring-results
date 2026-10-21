"""Standalone locked Gaze inference. No webcam, training or alert policy."""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
from PIL import Image
import torch
from torch import nn

CHECKPOINT_SHA256='9c6e90e7a50ad7dd5bafe2c7021b75bf4c3cc1be5ec27087b86b1568a9505717'
CLASSES=['center_mirror','front','front_right','infotainment','left','left_mirror','right','right_mirror','steering_wheel']


class Block(nn.Module):
    def __init__(self,cin,cout,stride=1):
        super().__init__()
        self.conv1=nn.Conv2d(cin,cout,3,stride,1,bias=False);self.bn1=nn.BatchNorm2d(cout)
        self.relu=nn.ReLU(inplace=True)
        self.conv2=nn.Conv2d(cout,cout,3,1,1,bias=False);self.bn2=nn.BatchNorm2d(cout)
        self.downsample=nn.Sequential(nn.Conv2d(cin,cout,1,stride,bias=False),nn.BatchNorm2d(cout)) if stride!=1 or cin!=cout else None
    def forward(self,x):
        residual=x if self.downsample is None else self.downsample(x)
        y=self.relu(self.bn1(self.conv1(x)));y=self.bn2(self.conv2(y))
        return self.relu(y+residual)


class Encoder(nn.Module):
    """ResNet18 layers matching the frozen torchvision checkpoint names."""
    def __init__(self):
        super().__init__()
        self.conv1=nn.Conv2d(3,64,7,2,3,bias=False);self.bn1=nn.BatchNorm2d(64)
        self.relu=nn.ReLU(inplace=True);self.maxpool=nn.MaxPool2d(3,2,1)
        self.layer1=nn.Sequential(Block(64,64),Block(64,64))
        self.layer2=nn.Sequential(Block(64,128,2),Block(128,128))
        self.layer3=nn.Sequential(Block(128,256,2),Block(256,256))
        self.layer4=nn.Sequential(Block(256,512,2),Block(512,512))
        self.avgpool=nn.AdaptiveAvgPool2d((1,1))
    def forward(self,x):
        x=self.maxpool(self.relu(self.bn1(self.conv1(x))))
        x=self.layer4(self.layer3(self.layer2(self.layer1(x))))
        return self.avgpool(x).flatten(1)


class FaceEyes(nn.Module):
    def __init__(self):super().__init__();self.encoder=Encoder()
    def forward(self,x):
        face,eye=x[:,:,:,:224],x[:,:,:,224:]
        black=x.new_tensor([-.485/.229,-.456/.224,-.406/.225])[None,:,None,None]
        present=((eye-black).abs().amax(dim=(1,2,3))>1e-5).to(x.dtype)[:,None]
        a,b=self.encoder(torch.cat([face,eye],0)).chunk(2,0)
        return torch.cat([a,b*present],1)


class Net(nn.Module):
    def __init__(self):
        super().__init__();self.backbone=FaceEyes()
        self.heads=nn.ModuleDict({'gaze':nn.Sequential(nn.Dropout(.2),nn.Linear(1024,9))})
    def forward(self,x):return self.heads['gaze'](self.backbone(x))


def tensor_from_pair(image):
    a=np.asarray(image)
    if a.shape!=(224,448,3) or a.dtype!=np.uint8:raise ValueError('Expected RGB uint8 pair, shape (224,448,3)')
    a=a.astype(np.float32)/255
    a=(a-np.array([.485,.456,.406],np.float32))/np.array([.229,.224,.225],np.float32)
    return torch.from_numpy(a.transpose(2,0,1).copy())


class GazePredictor:
    def __init__(self,checkpoint=None,device='cpu'):
        path=Path(checkpoint) if checkpoint else Path(__file__).with_name('best.pt')
        if hashlib.sha256(path.read_bytes()).hexdigest()!=CHECKPOINT_SHA256:raise ValueError('Checkpoint hash mismatch')
        c=torch.load(path,map_location='cpu',weights_only=True)
        if c['epoch']!=7 or c['config']['seed']!=43 or c['config']['classes']!={'gaze':CLASSES}:raise ValueError('Wrong model configuration')
        self.device=torch.device(device);self.model=Net()
        self.model.load_state_dict(c['state_dict'],strict=True);self.model.to(self.device).eval()
    @torch.inference_mode()
    def predict(self,rgb_pair):
        x=tensor_from_pair(rgb_pair)[None].to(self.device)
        p=self.model(x).softmax(1)[0].cpu().numpy();index=int(p.argmax())
        return dict(label=CLASSES[index],class_index=index,score=float(p[index]),
            probabilities={k:float(v) for k,v in zip(CLASSES,p)},
            eye_available=bool(np.asarray(rgb_pair)[:,224:].any()),
            note='Softmax scores are not calibrated confidence; no distraction alert decision.')


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--pair',required=True,help='Prepared RGB PNG: face left, eyes right, 448x224')
    p.add_argument('--checkpoint');p.add_argument('--device',default='cpu',choices=['cpu','cuda']);p.add_argument('--output')
    a=p.parse_args()
    with Image.open(a.pair) as im:result=GazePredictor(a.checkpoint,a.device).predict(np.array(im.convert('RGB')))
    text=json.dumps(result,indent=2)
    if a.output:Path(a.output).write_text(text)
    print(text)
