#!/usr/bin/env python3

import io
from picamera import PiCamera

##raspivid -o test1.h264 -t 20000 -ifx film -ISO 800 --shutter 28000 -awb auto -ex auto -fps 18 --mode 6
stream = io.BytesIO()
with PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate=18
    camera.start_preview()
    camera.start_recording(stream, format='h264', quality=20)
    camera.wait_recording(10)
    camera.stop_recording()

with open("test.h264", "wb") as f:
    f.write(stream.getvalue())

#ffmpeg -framerate 18 -i test.h264 -c copy output.mp4