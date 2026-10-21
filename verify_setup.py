"""Verify the frozen model bundle. Never opens a camera."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def verify(bundle):
    bundle=Path(bundle)
    assets=json.loads((ROOT/'config/model_assets.json').read_text())
    lock=json.loads((ROOT/'config/final_lock.json').read_text())
    for name,expected in assets['files'].items():
        path=bundle/name
        if not path.is_file():raise ValueError('Missing '+name+'. Run python scripts/download_models.py')
        if hashlib.sha256(path.read_bytes()).hexdigest()!=expected:raise ValueError('Hash mismatch: '+name)
    manifest=json.loads((bundle/'manifest.json').read_text())
    if manifest['models']!=lock['policy']['models']:raise ValueError('Model identity mismatch.')
    policy=json.loads((ROOT/'config/candidate_policy.json').read_text())
    if policy!=lock['policy']:raise ValueError('Policy differs from frozen final lock.')
    return lock

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--bundle',type=Path,default=ROOT/'models')
    p.add_argument('--smoke',action='store_true',help='Load all models and process synthetic blank frames.')
    a=p.parse_args();lock=verify(a.bundle)
    print('PASS: checkpoint, landmarker, manifest and final policy identities.')
    if a.smoke:
        import numpy as np
        import torch
        from driver_system.runtime import DriverSystem
        torch.set_num_threads(4)
        system=DriverSystem(a.bundle,policy_config=lock['policy'])
        try:
            result=system.process(np.zeros((480,640,3),np.uint8),0.0)
            assert not result['alerts']['active']
            assert result['alerts']['unknown']
            system.body_visible=True
            result=system.process(np.zeros((480,640,3),np.uint8),0.1)
            assert 'action' in result['predictions']
            gaze=system.gaze.predict(np.zeros((224,448,3),np.uint8))
            face=system.drowsiness.predict(np.zeros((224,224,3),np.uint8))
            for prediction in [gaze,*face.values(),result['predictions']['action']]:
                values=list(prediction['probabilities'].values())
                assert all(np.isfinite(values)) and abs(sum(values)-1)<1e-4
            print('PASS: synthetic missing-observation handling and all model forward passes. Not an accuracy test.')
        finally:system.close()

if __name__=='__main__':main()

