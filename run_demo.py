from util.analysis_realtime import analysis
import cv2
import numpy as np

# Initializing
cap = cv2.VideoCapture(0)
ana = analysis()

# Capture every frame and send to detector
while True:
    _, frame = cap.read()
    bm = ana.detect_face(frame)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
#  if 'q' is pressed == quit program
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
