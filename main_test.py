import cv2
import time
import numpy as np

cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('Input', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break


"""
Step 1:
- get background keyboard area
- define area that correspond to different keys: dict of each keyboard_key: <bounding_box>
- on any key input, analyze key that was pressed, then look at what fingertip is on said area
"""