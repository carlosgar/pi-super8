#!/usr/bin/env python3

import io
from picamera import PiCamera

camera = PiCamera()

stream = io.BytesIO()
with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_recording(stream, format='h264', quality=23)
    camera.wait_recording(15)
    camera.stop_recording()