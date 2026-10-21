"""Offline video runner. Does not open a webcam or play alarm audio."""
import argparse,json,time,hashlib
from pathlib import Path
import cv2
import numpy as np
import torch
from .runtime import DriverSystem

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--video',required=True);p.add_argument('--bundle',default='exports/driver_system_v1')
    p.add_argument('--output',required=True);p.add_argument('--sample-fps',type=float,default=10)
    p.add_argument('--device',choices=['cpu','cuda'],default='cpu');p.add_argument('--threads',type=int,default=4)
    p.add_argument('--body-visible',action='store_true');p.add_argument('--max-samples',type=int)
    p.add_argument('--policy',help='Optional validation-selected candidate JSON; defaults remain unchanged')
    a=p.parse_args()
    if not Path(a.video).is_file():raise ValueError('Provide a video file; camera devices are not supported')
    if not 2<=a.sample_fps<=30:raise ValueError('Sample FPS must be in [2,30]')
    if a.threads<1 or (a.max_samples is not None and a.max_samples<1):raise ValueError('Invalid limit')
    torch.set_num_threads(a.threads)
    out=Path(a.output);out.mkdir(parents=True,exist_ok=False)
    cap=cv2.VideoCapture(str(Path(a.video).resolve()))
    if not cap.isOpened():raise ValueError('Cannot open video')
    system=None;latencies=[];frames=0;sampled=0;last=None;next_sample=0;start=time.perf_counter();events=0
    try:
        policy=json.loads(Path(a.policy).read_text(encoding='utf-8')) if a.policy else None
        system=DriverSystem(a.bundle,a.device,a.body_visible,policy_config=policy)
        with (out/'predictions.jsonl').open('w',encoding='utf-8') as log,(out/'events.jsonl').open('w',encoding='utf-8') as eventlog:
            while True:
                ok,bgr=cap.read()
                if not ok:break
                frames+=1;t=cap.get(cv2.CAP_PROP_POS_MSEC)/1000
                if not np.isfinite(t) or (last is not None and t<=last):
                    raise ValueError('Video timestamps missing/non-increasing; repair or audit video before inference')
                last=t
                if t+1e-6<next_sample:continue
                next_sample=t+1/a.sample_fps
                begin=time.perf_counter();r=system.process(cv2.cvtColor(bgr,cv2.COLOR_BGR2RGB),t)
                elapsed=time.perf_counter()-begin;latencies.append(elapsed);sampled+=1;r['processing_ms']=elapsed*1000
                log.write(json.dumps(r)+'\n')
                if r['alerts']['started'] or r['alerts']['ended']:
                    eventlog.write(json.dumps({'timestamp_s':t,**r['alerts']})+'\n');events+=1
                if sampled%100==0:print(f'{sampled} samples; video {t:.1f}s',flush=True)
                if a.max_samples and sampled>=a.max_samples:break
        if not sampled:raise ValueError('No video samples decoded')
        summary={'status':'complete','video':str(Path(a.video).resolve()),'frames_decoded':frames,'samples':sampled,
         'last_timestamp_s':last,'requested_sample_fps':a.sample_fps,'body_visible_declared':a.body_visible,
         'wall_seconds_including_load':time.perf_counter()-start,'processing_ms_median':float(np.median(latencies)*1000),
         'processing_ms_p95':float(np.percentile(latencies,95)*1000),'sample_processing_fps':float(1/np.mean(latencies)),
         'event_transitions':events,'policy':system.manifest['policy'],'models':system.manifest['models'],
         'manifest_sha256':hashlib.sha256((Path(a.bundle)/'manifest.json').read_bytes()).hexdigest(),
         'limited_run':bool(a.max_samples and sampled>=a.max_samples),
         'limitations':['Offline throughput, not webcam FPS.','Processing latency excludes video decode and log I/O; wall time includes them.',
         'End-of-stream vs decode failure not distinguished by OpenCV.','Alerts experimental; no false alarms/hour or detection-delay evaluation.']}
        (out/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
        print(json.dumps(summary,indent=2))
    except Exception as e:
        (out/'FAILED.json').write_text(json.dumps({'error':str(e),'samples':sampled}),encoding='utf-8');raise
    finally:
        cap.release()
        if system:system.close()
if __name__=='__main__':main()
