import cv2
import pickle
import cvzone
import numpy as np
import os


# Video feed
cap = cv2.VideoCapture(os.path("car_parking.mp4"))

while True:
    success, img = cap.read()
    cv2.imshow("image", img)
    cv2.waitKey(1)
