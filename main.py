import cv2
import pickle
import cvzone
import numpy as np
import os


# Video feed
cap = cv2.VideoCapture('car_parking.mp4')

width, height = 40, 80

with open('parking_position', 'rb') as f:
    position_list = pickle.load(f)

while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = cap.read()
    for pos in position_list:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 0), 2)

    cv2.imshow("image", img)
    cv2.waitKey(10)
