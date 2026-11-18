"""Non-blocking Windows alert tone with wall-clock throttling."""
import math
import os
from pathlib import Path
import struct
import tempfile
import time
import wave


class AlertAudio:
    def __init__(self, enabled=False, repeat_s=5., play=None, stop=None, clock=time.monotonic, continuous=False):
        self.continuous = continuous
        self.enabled = enabled
        self.repeat_s = repeat_s
        self.clock = clock
        self.last_play = None
        self.previous = set()
        self.directory = None
        self.play = play
        self.stop = stop or (lambda: None)
        self.status = 'disabled'
        if not enabled:
            return
        if play is not None:
            self.status = 'test-backend'
            return
        if os.name != 'nt':
            self.enabled = False
            self.status = 'unavailable-platform'
            print('Audio unavailable: this demo tone currently supports Windows only.', flush=True)
            return
        try:
            import winsound
            self.directory = tempfile.TemporaryDirectory(prefix='driver-alert-')
            path = Path(self.directory.name)/'alert.wav'
            rate = 22050
            frames = bytearray()
            for i in range(int(rate*(.8 if continuous else .55))):
                t = i/rate
                tone = (0 <= t < .18) or (.28 <= t < .46)
                value = int(9000*math.sin(2*math.pi*880*t)) if tone else 0
                frames.extend(struct.pack('<h', value))
            with wave.open(str(path), 'wb') as out:
                out.setnchannels(1); out.setsampwidth(2); out.setframerate(rate)
                out.writeframes(frames)
            flags = winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NODEFAULT
            if continuous:flags |= winsound.SND_LOOP
            self.play = lambda: winsound.PlaySound(str(path), flags)
            self.stop = lambda: winsound.PlaySound(None, 0)
            self.status = 'ready-windows'
        except Exception as error:
            self.enabled = False
            self.status = 'unavailable-error'
            print('Audio initialization failed:', type(error).__name__, flush=True)

    def update(self, active):
        current = set(active)
        if not self.enabled:
            self.previous = current
            return
        now = self.clock()
        if not current:
            if self.previous:
                self._stop()
        elif (not self.previous if self.continuous else self.last_play is None or now-self.last_play >= self.repeat_s):
            try:
                self.play()
                self.last_play = now
            except Exception as error:
                self.enabled = False
                self.status = 'playback-error'
                print('Audio playback failed:', type(error).__name__, flush=True)
        self.previous = current

    def _stop(self):
        try:
            self.stop()
        except Exception as error:
            self.enabled = False
            self.status = 'playback-error'
            print('Audio stop failed:', type(error).__name__, flush=True)

    def close(self):
        self._stop()
        if self.directory is not None:
            try:
                self.directory.cleanup()
            except OSError as error:
                print('Audio temporary-file cleanup failed:', type(error).__name__, flush=True)
