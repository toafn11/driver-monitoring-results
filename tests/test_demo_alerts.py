import copy
import unittest
from driver_system.demo_alerts import YawnDemoAlert
from driver_system.demo_audio import AlertAudio


def sample(t,score=None,active=()):
    predictions={} if score is None else {'yawn':{'probabilities':{'no_yawn':1-score,'yawning_with_hand':score/2,'yawning_without_hand':score/2}}}
    return {'timestamp_s':t,'predictions':predictions,'alerts':{'active':list(active),'started':[], 'ended':[], 'unknown':[], 'status':'no_active_warning'}}


class DemoAlertTests(unittest.TestCase):
    def test_sustained_yawn_merges_without_mutating_research(self):
        policy=YawnDemoAlert()
        self.assertFalse(policy.update(sample(0,.8))['alerts']['active'])
        self.assertFalse(policy.update(sample(.5,.8))['alerts']['active'])
        source=sample(1,.8,('gaze_away',));before=copy.deepcopy(source)
        result=policy.update(source)
        self.assertEqual(source,before)
        self.assertEqual(result['alerts']['active'],['gaze_away','yawning'])
        self.assertEqual(result['alerts']['started'],['yawning'])
        self.assertEqual(result['research_alerts'],before['alerts'])
        self.assertEqual(policy.update(sample(1.1,.8))['alerts']['started'],[])

    def test_short_yawn_and_negative_reset(self):
        policy=YawnDemoAlert()
        for t,score in [(0,.8),(.5,.8),(.6,.1),(1,.8),(1.5,.8)]:
            self.assertNotIn('yawning',policy.update(sample(t,score))['alerts']['active'])

    def test_missing_invalid_and_gap_reset(self):
        policy=YawnDemoAlert()
        for t in [0,.5,1]:result=policy.update(sample(t,.8))
        self.assertIn('yawning',result['alerts']['active'])
        result=policy.update(sample(1.1))
        self.assertIn('yawning',result['alerts']['ended'])
        self.assertIn('yawning',result['alerts']['unknown'])
        self.assertFalse(policy.update(sample(4,.8))['alerts']['active'])
        bad=sample(4.1,.8);bad['predictions']['yawn']['probabilities']['no_yawn']=float('nan')
        self.assertIn('yawning',policy.update(bad)['alerts']['unknown'])

    def test_audio_uses_wall_clock_and_throttles_reactivation(self):
        now=[0.];played=[];stopped=[]
        audio=AlertAudio(True,play=lambda:played.append(now[0]),stop=lambda:stopped.append(True),clock=lambda:now[0])
        audio.update([]);self.assertFalse(played)
        audio.update(['yawning']);self.assertEqual(played,[0.])
        now[0]=1;audio.update(['yawning','eyes_closed']);self.assertEqual(len(played),1)
        audio.update([]);self.assertTrue(stopped)
        now[0]=2;audio.update(['yawning']);self.assertEqual(len(played),1)
        now[0]=5;audio.update(['yawning']);self.assertEqual(played,[0.,5])
        audio.close()

    def test_disabled_audio_and_backend_failure(self):
        audio=AlertAudio(False,play=lambda:self.fail('Disabled audio played'))
        audio.update(['yawning'])
        def fail():raise RuntimeError('no device')
        audio=AlertAudio(True,play=fail)
        audio.update(['yawning'])
        self.assertFalse(audio.enabled)
        self.assertEqual(audio.status,'playback-error')

    def test_stop_failure_does_not_interrupt_demo_cleanup(self):
        def fail():raise RuntimeError('no device')
        audio=AlertAudio(True,play=lambda:None,stop=fail)
        audio.update(['yawning'])
        audio.update([])
        self.assertFalse(audio.enabled)
        audio.close()

if __name__=='__main__':unittest.main()
