import unittest
from driver_system.window_policy import WindowPolicy,binary_signals,HEADS
class WindowTests(unittest.TestCase):
 def config(self):return {'max_gap_s':.6,'branches':{h:{'threshold':.7,'window_s':1.,'fraction':.5} for h in HEADS}}
 def test_group_probability(self):
  c=self.config();s=binary_signals({'gaze':{'probabilities':{'front':.2,'left':.4,'right':.4}}},c)
  self.assertIs(s['gaze_away'],True);self.assertIsNone(s['eyes_closed'])
 def test_absence_resets_and_gap(self):
  p=WindowPolicy(self.config())
  for t in [0,.5,1.]:r=p.update(t,{'eyes_closed':True})
  self.assertIn('eyes_closed',r['active'])
  self.assertIn('eyes_closed',p.update(1.1,{})['ended'])
  self.assertNotIn('eyes_closed',p.update(1.2,{'eyes_closed':True})['active'])
  self.assertNotIn('eyes_closed',p.update(5.,{'eyes_closed':True})['active'])
  with self.assertRaises(ValueError):p.update(5.,{})
 def test_time_not_frame_count(self):
  p=WindowPolicy(self.config())
  for i in range(50):self.assertFalse(p.update(i*.01,{'eyes_closed':True})['active'])
 def test_short_negative_does_not_erase_window(self):
  p=WindowPolicy(self.config())
  for t,v in [(0,True),(.2,True),(.4,False),(.5,True),(.7,True),(1.,True)]:r=p.update(t,{'eyes_closed':v})
  self.assertIn('eyes_closed',r['active'])
if __name__=='__main__':unittest.main()
