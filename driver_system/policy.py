"""Experimental temporal policy. No parameters were selected on test results."""
import math

DEFAULT_POLICY={'status':'experimental_not_validation_calibrated','max_gap_s':0.6,
 'min_score':0.7,'hold_s':{'eyes_closed':1.5,'gaze_away':2.0,'distracted_action':2.0}}

class TemporalPolicy:
    def __init__(self,config=None):
        self.config=config or DEFAULT_POLICY
        if not 0<=self.config['min_score']<=1 or self.config['max_gap_s']<=0:raise ValueError('Invalid policy')
        if any(v<=0 for v in self.config['hold_s'].values()):raise ValueError('Invalid duration')
        self.last=None;self.since={};self.active=set()
    def update(self,t,signals):
        if not math.isfinite(t) or (self.last is not None and t<=self.last):raise ValueError('Timestamps must increase')
        gap=self.last is not None and t-self.last>self.config['max_gap_s']
        if gap:self.since.clear()
        old=self.active;active=set();unknown=[]
        for name,hold in self.config['hold_s'].items():
            value=signals.get(name)
            if value is None:unknown.append(name)
            if value is True:
                self.since.setdefault(name,t)
                if t-self.since[name]>=hold:active.add(name)
            else:self.since.pop(name,None)
        self.last=t;self.active=active
        return dict(active=sorted(active),started=sorted(active-old),ended=sorted(old-active),unknown=unknown,
                    status='warning' if active else ('unknown' if unknown else 'no_active_warning'),
                    experimental=True)

def signals_from_predictions(predictions,min_score):
    def classify(head,positive):
        p=predictions.get(head)
        if p is None or p['score']<min_score:return None
        return p['label'] in positive
    return {'eyes_closed':classify('eyes',{'close'}),
            'gaze_away':classify('gaze',{'center_mirror','front_right','infotainment','left','left_mirror','right','right_mirror','steering_wheel'}),
            'distracted_action':classify('action',{'drinking','hair_and_makeup','phonecall_left','phonecall_right','radio','reach_backseat','reach_side','talking_to_passenger','texting_left','texting_right'})}
