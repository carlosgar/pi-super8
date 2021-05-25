#!/usr/bin/env python3

import io
from picamera import PiCamera

stream = io.BytesIO()
with PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_recording(stream, format='h264', quality=23)
    camera.wait_recording(5)
    camera.stop_recording()

with open("test.h264", "wb") as f:
    f.write(stream.getvalue())