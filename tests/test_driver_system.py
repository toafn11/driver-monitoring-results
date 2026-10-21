import unittest
from driver_system.policy import TemporalPolicy,signals_from_predictions
class PolicyTests(unittest.TestCase):
 def test_duration_missing_and_rearm(self):
  p=TemporalPolicy();s={'eyes_closed':True,'gaze_away':False,'distracted_action':False}
  for t in [0,.5,1]:self.assertFalse(p.update(t,s)['active'])
  self.assertEqual(p.update(1.5,s)['started'],['eyes_closed'])
  self.assertFalse(p.update(2,s)['started'])
  s['eyes_closed']=None
  r=p.update(2.5,s);self.assertEqual(r['ended'],['eyes_closed']);self.assertIn('eyes_closed',r['unknown'])
  s['eyes_closed']=True
  self.assertFalse(p.update(3,s)['active'])
 def test_gaps_and_time(self):
  p=TemporalPolicy();s={'eyes_closed':True}
  p.update(0,s);self.assertFalse(p.update(5,s)['active'])
  with self.assertRaises(ValueError):p.update(5,s)
  with self.assertRaises(ValueError):p.update(float('nan'),s)
 def test_no_face_low_score_not_safe(self):
  s=signals_from_predictions({'eyes':{'label':'close','score':.6}},.7)
  self.assertTrue(all(v is None for v in s.values()))
  s=signals_from_predictions({'eyes':{'label':'open','score':.9},'yawn':{'label':'yawning_with_hand','score':1}},.7)
  self.assertIs(s['eyes_closed'],False);self.assertNotIn('yawn',s)
if __name__=='__main__':unittest.main()
