import unittest
from driver_system.demo_alerts import ObservationDemoAlert,YawnDemoAlert
from driver_system.demo_audio import AlertAudio


def frame(t,face=True,nose=.4,center=.3,scale=.2):
    return {'timestamp_s':t,'quality':{'face_available':face,'demo_geometry':{'nose_ratio':nose,'center_y':center,'face_scale':scale}},
            'predictions':{},'alerts':{'active':[],'started':[],'ended':[],'unknown':[],'status':'no_active_warning'}}


class ObservationTests(unittest.TestCase):
    def test_recalibration_clears_old_posture_warning_and_locks_new_reference(self):
        p=self.calibrated()
        for t in [2.5,3,3.5]:p.update(frame(t,nose=.6))
        p.active.add('driver_not_visible')
        self.assertIn('head_lowered',p.active)
        p.start_calibration()
        self.assertNotIn('head_lowered',p.active)
        self.assertIn('driver_not_visible',p.active)
        for t in [4,4.5,5,5.5,6]:
            p.start_calibration()  # Key auto-repeat must not restart collection.
            p.update(frame(t,nose=.45))
        self.assertEqual(p.calibration_status()['state'],'LOCKED')
        self.assertEqual(p.calibration_revision,2)
        self.assertAlmostEqual(p.baseline['nose_ratio'],.45)
        p.reset_calibration()
        self.assertEqual(p.calibration_status()['state'],'NOT SET')
        self.assertIsNone(p.baseline)
        self.assertEqual(ObservationDemoAlert().calibration_revision,0)
        self.assertIsNone(ObservationDemoAlert().baseline)

    def test_calibration_progress_and_missing_face_message(self):
        p=ObservationDemoAlert();p.start_calibration()
        p.update(frame(0));p.update(frame(.5))
        self.assertAlmostEqual(p.calibration_status()['progress'],.25)
        p.update(frame(1,False))
        self.assertEqual(p.calibration_status()['progress'],0)
        self.assertIn('visible face',p.calibration_status()['note'])

    def test_geometry_is_relative_and_rejects_invalid_landmarks(self):
        from types import SimpleNamespace
        from driver_system.preprocess import demo_geometry
        points=[SimpleNamespace(x=.5,y=.4) for _ in range(468)]
        points[33]=SimpleNamespace(x=.4,y=.3)
        points[263]=SimpleNamespace(x=.6,y=.3)
        points[152]=SimpleNamespace(x=.5,y=.7)
        points[1]=SimpleNamespace(x=.5,y=.46)
        self.assertAlmostEqual(demo_geometry(points)['nose_ratio'],.4)
        for p in points:p.y+=.1
        self.assertAlmostEqual(demo_geometry(points)['nose_ratio'],.4)
        self.assertAlmostEqual(demo_geometry(points)['center_y'],.4)
        points[1].x=float('nan')
        self.assertIsNone(demo_geometry(points))
        self.assertIsNone(demo_geometry([]))

    def calibrated(self):
        p=ObservationDemoAlert();p.start_calibration()
        for t in [0,.5,1,1.5,2]:p.update(frame(t))
        self.assertIsNotNone(p.baseline)
        return p

    def test_no_face_warning_and_stable_recovery(self):
        p=ObservationDemoAlert()
        for t in [0,.5,1,1.5]:self.assertFalse(p.update(frame(t,False))['alerts']['active'])
        self.assertIn('driver_not_visible',p.update(frame(2,False))['alerts']['started'])
        self.assertIn('driver_not_visible',p.update(frame(2.1))['alerts']['active'])
        self.assertIn('driver_not_visible',p.update(frame(2.3,False))['alerts']['active'])
        p.update(frame(2.4))
        self.assertIn('driver_not_visible',p.update(frame(2.9))['alerts']['ended'])

    def test_head_lowering_missing_face_keeps_warning_and_recovery(self):
        p=self.calibrated()
        for t in [2.5,3,3.5]:r=p.update(frame(t,nose=.6))
        self.assertIn('head_lowered',r['alerts']['active'])
        r=p.update(frame(4,False))
        self.assertIn('head_lowered',r['alerts']['active'])
        self.assertIn('head_lowered',r['alerts']['unknown'])
        p.update(frame(4.5))
        self.assertIn('head_lowered',p.update(frame(5))['alerts']['ended'])

    def test_sinking_and_scale_guard(self):
        p=self.calibrated()
        for t in [2.5,3,3.5]:r=p.update(frame(t,center=.45))
        self.assertIn('head_lowered',r['alerts']['active'])
        p=self.calibrated()
        for t in [2.5,3,3.5]:r=p.update(frame(t,center=.45,scale=.5))
        self.assertNotIn('head_lowered',r['alerts']['active'])
        self.assertIn('head_lowered',r['alerts']['unknown'])

    def test_requires_explicit_calibration_and_resets_on_missing_or_gap(self):
        p=ObservationDemoAlert()
        for t in [0,.5,1,1.5,2]:p.update(frame(t))
        self.assertIsNone(p.baseline)
        p.start_calibration();p.update(frame(2.5));p.update(frame(3,False))
        p.update(frame(3.5));p.update(frame(5))
        self.assertIsNone(p.baseline)
        for t in [5.5,6,6.5,7]:p.update(frame(t))
        self.assertIsNotNone(p.baseline)

    def test_gap_does_not_count_as_observed_missing_time(self):
        p=ObservationDemoAlert();p.update(frame(0,False))
        self.assertFalse(p.update(frame(8,False))['alerts']['active'])
        with self.assertRaises(ValueError):p.update(frame(8,False))

    def test_research_alerts_preserved_across_extensions(self):
        src=frame(0)
        yawn=YawnDemoAlert().update(src)
        combined=ObservationDemoAlert().update(yawn)
        self.assertEqual(combined['research_alerts'],src['alerts'])
        self.assertNotIn('research_alerts',src)

    def test_continuous_audio_starts_once_stops_and_restarts_immediately(self):
        played=[];stopped=[]
        audio=AlertAudio(True,continuous=True,play=lambda:played.append(1),stop=lambda:stopped.append(1))
        for _ in range(100):audio.update(['head_lowered'])
        self.assertEqual(len(played),1)  # Native backend loops independently of inference.
        audio.update(['driver_not_visible']);self.assertEqual(len(played),1)
        audio.update([]);self.assertEqual(len(stopped),1)
        audio.update(['yawning']);self.assertEqual(len(played),2)
        audio.close();self.assertEqual(len(stopped),2)

if __name__=='__main__':unittest.main()
