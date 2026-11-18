"""Original RGB frame -> same face/eye pair as prepared DMD data. No webcam."""
from pathlib import Path
import hashlib
import cv2
import numpy as np
def crop_box(landmarks,width,height):
    xy=np.array([(p.x*width,p.y*height) for p in landmarks])
    if not len(xy) or not np.isfinite(xy).all():return None
    lo,hi=xy.min(0),xy.max(0)
    side=min(int(np.ceil(max(hi-lo)*1.4)),width,height)
    if side<24:return None
    cx,cy=(lo+hi)/2
    x=max(0,min(width-side,int(cx-side/2)));y=max(0,min(height-side,int(cy-side/2)))
    return x,y,x+side,y+side

def letterbox(image,size):
    h,w=image.shape[:2];scale=size/max(h,w)
    small=cv2.resize(image,(max(1,round(w*scale)),max(1,round(h*scale))))
    canvas=np.zeros((size,size,3),np.uint8)
    y=(size-small.shape[0])//2;x=(size-small.shape[1])//2
    canvas[y:y+small.shape[0],x:x+small.shape[1]]=small
    return canvas

def eye_box(points,w,h):
    # Both eye corners and upper/lower lids; same geometry for every class/person.
    ids=[33,133,159,145,362,263,386,374]
    if len(points)<=max(ids):return None
    xy=np.array([(points[i].x*w,points[i].y*h) for i in ids])
    if not np.isfinite(xy).all():return None
    lo,hi=xy.min(0),xy.max(0);width=(hi[0]-lo[0])*1.35
    height=max((hi[1]-lo[1])*2.0,width*.40)
    if width<16 or height<8:return None
    cx,cy=(lo+hi)/2
    box=(max(0,int(cx-width/2)),max(0,int(cy-height/2)),min(w,int(np.ceil(cx+width/2))),min(h,int(np.ceil(cy+height/2))))
    return box if box[2]>box[0] and box[3]>box[1] else None

def demo_geometry(points):
    """Image-space posture cues, not head-pose angles or trained predictions."""
    if len(points)<264:return None
    xy=np.array([(p.x,p.y) for p in points],dtype=float)
    if not np.isfinite(xy).all():return None
    eyes=(xy[33]+xy[263])/2
    axis=xy[152]-eyes
    length=float(np.linalg.norm(axis))
    if length<.03:return None
    return {'nose_ratio':float(np.dot(xy[1]-eyes,axis)/(length*length)),
            'center_y':float(eyes[1]),'face_scale':length}

class PairPreprocessor:
    def __init__(self,model_path=None):
        import mediapipe as mp
        self.mp=mp
        path=Path(model_path) if model_path else Path(__file__).with_name('face_landmarker.task')
        if hashlib.sha256(path.read_bytes()).hexdigest()!=ASSET_SHA256:raise ValueError('Landmarker asset hash mismatch')
        options=mp.tasks.vision.FaceLandmarkerOptions(base_options=mp.tasks.BaseOptions(model_asset_path=str(path)),
            running_mode=mp.tasks.vision.RunningMode.IMAGE,num_faces=1,min_face_detection_confidence=.5,min_face_presence_confidence=.5)
        self.detector=mp.tasks.vision.FaceLandmarker.create_from_options(options)
    def process(self,rgb):
        if rgb.ndim!=3 or rgb.shape[2]!=3 or rgb.dtype!=np.uint8:raise ValueError('Expected RGB uint8 image')
        detected=self.detector.detect(self.mp.Image(image_format=self.mp.ImageFormat.SRGB,data=np.ascontiguousarray(rgb)))
        points=detected.face_landmarks[0] if detected.face_landmarks else []
        h,w=rgb.shape[:2];face_box=crop_box(points,w,h) if points else None
        eyes=eye_box(points,w,h) if points else None
        bgr=cv2.cvtColor(rgb,cv2.COLOR_RGB2BGR)
        face=bgr
        if face_box:
            x0,y0,x1,y1=face_box;face=bgr[y0:y1,x0:x1]
        face=letterbox(face,224)
        # Training face pixels were decoded JPEG quality 90 before PNG pairing.
        ok,encoded=cv2.imencode('.jpg',face,[cv2.IMWRITE_JPEG_QUALITY,90])
        if not ok:raise ValueError('JPEG encoding failed')
        face=cv2.imdecode(encoded,cv2.IMREAD_COLOR)
        eye=np.zeros((224,224,3),np.uint8)
        if eyes:
            x0,y0,x1,y1=eyes;eye=letterbox(bgr[y0:y1,x0:x1],224)
        return cv2.cvtColor(np.concatenate([face,eye],1),cv2.COLOR_BGR2RGB),dict(face_available=bool(face_box),eye_available=bool(eyes),demo_geometry=demo_geometry(points) if face_box else None)
    def close(self):self.detector.close()
    def __enter__(self):return self
    def __exit__(self,*args):self.close()

ASSET_SHA256='64184e229b263107bc2b804c6625db1341ff2bb731874b0bcc2fe6544e0bc9ff'
