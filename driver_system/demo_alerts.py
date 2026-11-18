"""Optional demonstration alerts. Does not modify the frozen research policy."""
import copy
import math
import statistics
from .policy import TemporalPolicy


class YawnDemoAlert:
    def __init__(self, threshold=.7, hold_s=1., max_gap_s=.6):
        self.config = {'version': 'demo-yawn-v1', 'threshold': threshold,
                       'hold_s': hold_s, 'max_gap_s': max_gap_s,
                       'validated': False}
        self.policy = TemporalPolicy({'min_score': threshold, 'max_gap_s': max_gap_s,
                                      'hold_s': {'yawning': hold_s}})

    def update(self, result):
        prediction = result['predictions'].get('yawn')
        score = None
        if prediction is not None:
            probs = prediction['probabilities']
            values = [probs.get(k) for k in ('no_yawn', 'yawning_with_hand', 'yawning_without_hand')]
            if all(isinstance(v, (int, float)) and math.isfinite(v) and 0 <= v <= 1 for v in values):
                if abs(sum(values)-1) <= 1e-4:
                    score = values[1] + values[2]
        signals = {'yawning': None if score is None else score >= self.config['threshold']}
        extra = self.policy.update(result['timestamp_s'], signals)
        merged = copy.deepcopy(result)
        merged['research_alerts'] = copy.deepcopy(result.get('research_alerts',result['alerts']))
        for key in ('active', 'started', 'ended', 'unknown'):
            merged['alerts'][key] = sorted(set(result['alerts'][key]) | set(extra[key]))
        alerts = merged['alerts']
        alerts['status'] = 'warning' if alerts['active'] else ('unknown' if alerts['unknown'] else 'no_active_warning')
        merged['demo_yawn'] = {'config': self.config, 'score': score, 'signal': signals['yawning']}
        return merged


class ObservationDemoAlert:
    """Optional, unvalidated posture and visibility monitoring with clear recovery."""
    def __init__(self):
        self.config={'version':'demo-observation-v1','validated':False,
                     'face_missing_s':2.,'head_lowered_s':1.,'recovery_s':.5,
                     'max_gap_s':1.,'calibration_s':2.,'nose_delta':.12,'center_drop':.12}
        self.last=None;self.since={};self.clear_since={};self.active=set()
        self.baseline=None;self.calibrating=False;self.calibration=[]

    def start_calibration(self):
        self.baseline=None;self.calibrating=True;self.calibration=[]
        self.since.pop('head_lowered',None)

    @staticmethod
    def valid_geometry(g):
        return isinstance(g,dict) and all(isinstance(g.get(k),(int,float)) and math.isfinite(g[k]) for k in ('nose_ratio','center_y','face_scale')) and g['face_scale']>.03

    def update(self,result):
        t=result['timestamp_s']
        if not math.isfinite(t) or (self.last is not None and t<=self.last):raise ValueError('Timestamps must increase')
        gap=self.last is not None and t-self.last>self.config['max_gap_s']
        if gap:
            self.since.clear();self.clear_since.clear();self.calibration=[]
        self.last=t
        quality=result.get('quality',{})
        face=quality.get('face_available')
        g=quality.get('demo_geometry') if face is True else None
        if not self.valid_geometry(g):g=None
        if self.calibrating:
            if g is None:self.calibration=[]
            else:
                self.calibration.append((t,g.copy()))
                # Require a stable, operator-requested forward-looking baseline.
                while self.calibration and t-self.calibration[0][0]>2.5:self.calibration.pop(0)
                values=[v for _,v in self.calibration]
                stable=all(max(v[k] for v in values)-min(v[k] for v in values)<limit for k,limit in [('nose_ratio',.08),('center_y',.05)])
                if not stable:self.calibration=[(t,g.copy())]
                elif len(values)>=5 and t-self.calibration[0][0]>=self.config['calibration_s']:
                    self.baseline={k:statistics.median(v[k] for v in values) for k in g}
                    self.calibrating=False;self.calibration=[]
        lowered=None
        if g is not None and self.baseline is not None:
            scale=g['face_scale']/self.baseline['face_scale']
            if .7<=scale<=1.4:
                lowered=(g['nose_ratio']-self.baseline['nose_ratio']>=self.config['nose_delta'] or
                         g['center_y']-self.baseline['center_y']>=self.config['center_drop'])
        signals={'driver_not_visible':None if not isinstance(face,bool) else not face,'head_lowered':lowered}
        old=set(self.active)
        for name,hold in [('driver_not_visible',self.config['face_missing_s']),('head_lowered',self.config['head_lowered_s'])]:
            value=signals[name]
            if value is True:
                self.clear_since.pop(name,None);self.since.setdefault(name,t)
                if t-self.since[name]+1e-9>=hold:self.active.add(name)
            elif value is False:
                self.since.pop(name,None);self.clear_since.setdefault(name,t)
                if t-self.clear_since[name]+1e-9>=self.config['recovery_s']:self.active.discard(name)
            else:
                # Missing evidence must not silently clear an established posture warning.
                self.since.pop(name,None);self.clear_since.pop(name,None)
        merged=copy.deepcopy(result)
        merged['research_alerts']=copy.deepcopy(result.get('research_alerts',result['alerts']))
        extra={'active':self.active,'started':self.active-old,'ended':old-self.active,
               'unknown':{k for k,v in signals.items() if v is None}}
        for key in extra:merged['alerts'][key]=sorted(set(result['alerts'][key])|set(extra[key]))
        alerts=merged['alerts'];alerts['status']='warning' if alerts['active'] else ('unknown' if alerts['unknown'] else 'no_active_warning')
        merged['demo_observation']={'config':self.config.copy(),'signals':signals,
            'calibration':'collecting: look forward, stay still' if self.calibrating else ('ready' if self.baseline else 'required: look forward and press C'),
            'baseline':self.baseline,'geometry':g}
        return merged
