import unittest
from driver_system.action_policy import ActionHysteresis,GROUPS
class HysteresisTests(unittest.TestCase):
 def config(self):return {'thresholds':{'phone':.8,'other':.9,'talk':.95},'hold_s':.5,'group_hold_s':{'talk':1.},'release_s':.3,'off_margin':.1,'cooldown_s':1.,'bridge_s':.2,'max_gap_s':.6}
 def p(self,label):
  probs={k:0. for k in set.union(*GROUPS.values(),{'safe_drive'})};probs[label]=1.
  return {'probabilities':probs}
 def test_latch_release_missing(self):
  p=ActionHysteresis(self.config());phone=self.p('phonecall_left');safe=self.p('safe_drive')
  p.update(0,phone);p.update(.3,phone);self.assertTrue(p.update(.6,phone)['started'])
  self.assertTrue(p.update(.7,safe)['active']);self.assertTrue(p.update(1.1,safe)['ended'])
  self.assertFalse(p.update(1.2,phone)['active'])
  self.assertTrue(p.update(1.3,None)['unknown'])
  self.assertFalse(p.update(1.4,phone)['active'])
 def test_gap_talk_and_timestamp(self):
  p=ActionHysteresis(self.config());talk=self.p('talking_to_passenger')
  for t in [0,.3,.6]:self.assertFalse(p.update(t,talk)['active'])
  self.assertFalse(p.update(3,talk)['active'])
  with self.assertRaises(ValueError):p.update(3,talk)
 def test_groups_exhaustive_disjoint(self):
  self.assertEqual(len(set.union(*GROUPS.values())),10)
  self.assertEqual(sum(map(len,GROUPS.values())),10)
if __name__=='__main__':unittest.main()
