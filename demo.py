"""Local visual demo using the frozen policy; no footage is uploaded or recorded."""
import argparse
import json
from pathlib import Path
import time
from verify_setup import ROOT, verify

def parse_args(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    source=p.add_mutually_exclusive_group(required=True)
    source.add_argument('--camera',type=int,help='Local webcam index, usually 0 or 1.')
    source.add_argument('--video',type=Path,help='Local video file.')
    p.add_argument('--bundle',type=Path,default=ROOT/'models')
    p.add_argument('--device',choices=['cpu','cuda'],default='cpu')
    p.add_argument('--body-visible',action='store_true',help='Enable action inference only when torso/hands are visible.')
    p.add_argument('--sample-fps',type=float,default=10)
    p.add_argument('--threads',type=int,default=4)
    p.add_argument('--headless',action='store_true',help='Video-only mode without a display window.')
    p.add_argument('--max-samples',type=int)
    p.add_argument('--log-dir',type=Path,help='Optional local JSON logs; images are not saved.')
    a=p.parse_args(argv)
    if not 2<=a.sample_fps<=30:p.error('--sample-fps must be between 2 and 30.')
    if a.threads<1 or (a.max_samples is not None and a.max_samples<1):p.error('Limits must be positive.')
    if a.headless and a.camera is not None:p.error('Use a visible preview for webcam demos.')
    if a.video is not None and not a.video.is_file():p.error('Video file does not exist.')
    return a

def overlay(frame,result,body_enabled,processing_ms):
    import cv2
    canvas=cv2.resize(frame,(min(1000,frame.shape[1]),max(1,round(frame.shape[0]*min(1000,frame.shape[1])/frame.shape[1]))))
    active=result['alerts']['active']
    lines=['RESEARCH DEMO | Q or Esc: quit | No video recording',
           'ALERT: '+(', '.join(active) if active else 'none (not a safety guarantee)'),
           'Unknown: '+(', '.join(result['alerts']['unknown']) or 'none'),
           'Action branch: '+('ENABLED - body view declared by operator' if body_enabled else 'DISABLED - face-only demo')]
    lines += [h+': '+p['label']+'  '+format(p['score'],'.2f') for h,p in result['predictions'].items()]
    lines += ['Inference: '+format(processing_ms,'.0f')+' ms | Webcam performance not validated']
    wrapped=[]
    for i,line in enumerate(lines):
        color=(70,70,255) if i==1 and active else (230,230,230)
        current=''
        for word in line.split():
            candidate=(current+' '+word).strip()
            if current and cv2.getTextSize(candidate,cv2.FONT_HERSHEY_SIMPLEX,.46,1)[0][0]>canvas.shape[1]-20:
                wrapped.append((current,color));current=word
            else:current=candidate
        wrapped.append((current,color))
    panel=cv2.copyMakeBorder(canvas,0,len(wrapped)*20+12,0,0,cv2.BORDER_CONSTANT,value=(18,18,18))
    for i,(line,color) in enumerate(wrapped):
        cv2.putText(panel,line,(10,canvas.shape[0]+20+i*20),cv2.FONT_HERSHEY_SIMPLEX,.46,color,1,cv2.LINE_AA)
    return panel

def run(args):
    import cv2
    import torch
    from driver_system.runtime import DriverSystem
    lock=verify(args.bundle)
    torch.set_num_threads(args.threads)
    if args.device=='cuda' and not torch.cuda.is_available():raise ValueError('CUDA unavailable. Use --device cpu.')
    system=None;cap=None;log=None;samples=0;last=None;next_sample=0.;result=None;ms=0.
    started=time.monotonic()
    try:
        system=DriverSystem(args.bundle,args.device,args.body_visible,policy_config=lock['policy'])
        cap=cv2.VideoCapture(args.camera if args.camera is not None else str(args.video))
        if not cap.isOpened():raise ValueError('Cannot open input. Check camera permissions/index or video codec.')
        if args.log_dir:
            args.log_dir.mkdir(parents=True,exist_ok=False)
            log=(args.log_dir/'predictions.jsonl').open('w',encoding='utf-8')
        clock_start=time.monotonic()
        while True:
            ok,frame=cap.read()
            if not ok:
                if args.camera is not None:raise RuntimeError('Camera read failed; no further observation is available.')
                break
            t=time.monotonic()-clock_start if args.camera is not None else cap.get(cv2.CAP_PROP_POS_MSEC)/1000
            if not __import__('math').isfinite(t) or (last is not None and t<=last):
                raise ValueError('Non-increasing timestamps. Audit or repair the input video.')
            last=t
            if t+1e-6>=next_sample:
                begin=time.perf_counter()
                result=system.process(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB),t)
                ms=(time.perf_counter()-begin)*1000
                next_sample=t+1/args.sample_fps;samples+=1
                if log:log.write(json.dumps({**result,'processing_ms':ms})+'\n')
                if result['alerts']['started']:print('Alert at',round(t,2),':',', '.join(result['alerts']['started']),flush=True)
            if not args.headless and result:
                cv2.imshow('Driver Monitoring - Experimental Demo',overlay(frame,result,args.body_visible,ms))
                if cv2.waitKey(1)&0xff in (ord('q'),ord('Q'),27):break
                if cv2.getWindowProperty('Driver Monitoring - Experimental Demo',cv2.WND_PROP_VISIBLE)<1:break
            if args.max_samples and samples>=args.max_samples:break
        if not samples:raise RuntimeError('No samples processed.')
        summary={'samples':samples,'wall_seconds':time.monotonic()-started,'source_type':'camera' if args.camera is not None else 'video',
                 'policy_sha256':lock['policy_sha256'],'body_visible_declared':args.body_visible,
                 'limited_run':bool(args.max_samples and samples>=args.max_samples),
                 'status':'completed','note':'Demo run, not labeled evaluation. Video EOF and decode failure are not distinguished by OpenCV.'}
        if args.log_dir:(args.log_dir/'demo_summary.json').write_text(json.dumps(summary,indent=2))
        print(json.dumps(summary,indent=2))
    finally:
        if log:log.close()
        if cap is not None:cap.release()
        if system is not None:system.close()
        if not args.headless:cv2.destroyAllWindows()

if __name__=='__main__':run(parse_args())

