"""Time-weighted window policy; absent observations reset evidence, never count as positive."""
from collections import deque
import math

HEADS={'eyes_closed':('eyes','open'),'gaze_away':('gaze','front'),'distracted_action':('action','safe_drive')}

def binary_signals(predictions,config):
    result={}
    for signal,(head,negative) in HEADS.items():
        p=predictions.get(head)
        if p is None:result[signal]=None;continue
        probs=p['probabilities']
        if negative not in probs or any(not math.isfinite(v) or not 0<=v<=1 for v in probs.values()):raise ValueError('Invalid probabilities')
        score=1-probs[negative]
        result[signal]=score>=config['branches'][signal]['threshold']
    return result

class WindowPolicy:
    def __init__(self,config):
        self.config=config;self.last=None;self.active=set();self.queues={h:deque() for h in HEADS}
        if config['max_gap_s']<=0:raise ValueError('Invalid gap')
        for c in config['branches'].values():
            if c['window_s']<=0 or not 0<c['fraction']<=1 or not 0<=c['threshold']<=1:raise ValueError('Invalid policy')
    def update(self,t,signals):
        if not math.isfinite(t) or (self.last is not None and t<=self.last):raise ValueError('Timestamps must increase')
        gap=self.last is not None and t-self.last>self.config['max_gap_s']
        active=set();unknown=[]
        for h,q in self.queues.items():
            c=self.config['branches'][h];v=signals.get(h)
            if gap or v is None:q.clear()
            if v is None:unknown.append(h);continue
            q.append((t,v));cut=t-c['window_s']
            while len(q)>1 and q[1][0]<=cut:q.popleft()
            if q[0][0]>cut+1e-8:continue
            points=list(q);positive=0.
            for (ta,va),(tb,vb) in zip(points,points[1:]):
                # Conservative: credit time only when both observations are positive.
                if va and vb:positive+=max(0.,tb-max(ta,cut))
            if v is True and positive/c['window_s']>=c['fraction']-1e-8:active.add(h)
        old=self.active;self.active=active;self.last=t
        return {'active':sorted(active),'started':sorted(active-old),'ended':sorted(old-active),'unknown':unknown,
                'status':'warning' if active else ('unknown' if unknown else 'no_active_warning'),'experimental':True}
