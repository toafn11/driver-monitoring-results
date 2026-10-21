"""Action-group hysteresis for validation experiments, never treats missing observations as safe."""
import math
GROUPS={'phone':{'phonecall_left','phonecall_right','texting_left','texting_right'},'other':{'drinking','hair_and_makeup','radio','reach_backseat','reach_side'},'talk':{'talking_to_passenger'}}
class ActionHysteresis:
 def __init__(self,c):
  self.c=c;self.last=None;self.active=False;self.cooldown_until=-1.;self.reset()
  if c['hold_s']<=0 or c['release_s']<0 or c['cooldown_s']<0:raise ValueError('Invalid times')
  for x in c['thresholds'].values():
   if not 0<=x-c['off_margin']<x<=1:raise ValueError('Invalid hysteresis')
 def reset(self):
  self.evidence={g:0. for g in GROUPS};self.previous={g:False for g in GROUPS};self.dip_since={g:None for g in GROUPS};self.low_since=None
 def update(self,t,p):
  if not math.isfinite(t) or (self.last is not None and t<=self.last):raise ValueError('Timestamps must increase')
  dt=0 if self.last is None else t-self.last;gap=dt>self.c['max_gap_s'];self.last=t;old=self.active
  if gap or p is None:
   self.active=False;self.reset()
   if p is None:return {'active':False,'started':False,'ended':old,'unknown':True,'signal':None}
   dt=0
  probs=p['probabilities']
  if any(not math.isfinite(v) or not 0<=v<=1 for v in probs.values()) or abs(sum(probs.values())-1)>1e-4:raise ValueError('Invalid probability vector')
  if not set.union(*GROUPS.values(),{'safe_drive'})<=set(probs):raise ValueError('Missing action class')
  scores={g:sum(probs[k] for k in labels) for g,labels in GROUPS.items()}
  if self.active:
   low=all(scores[g]<self.c['thresholds'][g]-self.c['off_margin'] for g in GROUPS)
   if low:
    if self.low_since is None:self.low_since=t
    if t-self.low_since>=self.c['release_s']:
     self.active=False;self.cooldown_until=t+self.c['cooldown_s'];self.reset()
   else:self.low_since=None
  else:
   for g,score in scores.items():
    high=score>=self.c['thresholds'][g]
    if high:
     if self.previous[g]:self.evidence[g]+=dt
     self.dip_since[g]=None
    else:
     if self.dip_since[g] is None:self.dip_since[g]=t
     if t-self.dip_since[g]>=self.c['bridge_s']:self.evidence[g]=0.
    self.previous[g]=high
   if t>=self.cooldown_until and any(self.evidence[g]>=self.c.get('group_hold_s',{}).get(g,self.c['hold_s']) for g in GROUPS):self.active=True
  return {'active':self.active,'started':self.active and not old,'ended':old and not self.active,'unknown':False,'signal':any(scores[g]>=self.c['thresholds'][g] for g in GROUPS)}

def merge_action_alerts(alerts,state):
 result={**alerts}
 for key,flag in [('active','active'),('started','started'),('ended','ended'),('unknown','unknown')]:
  result[key]=sorted(set(alerts[key])-{'distracted_action'}|({'distracted_action'} if state[flag] else set()))
 result['status']='warning' if result['active'] else ('unknown' if result['unknown'] else 'no_active_warning')
 return result
