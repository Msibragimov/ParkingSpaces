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


def check_spaces(img_proc):
    space_counter = 0
    for pos in position_list:
        x, y = pos
        img_crop = img_proc[y: y + height, x: x + width]
        # cv2.imshow(str(x * y), img_crop)
        count = cv2.countNonZero(img_crop)
        cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=0.8, thickness=1, offset=0, colorR=(0, 0, 255))

        if count < 400:
            color = (0, 255, 0)
            thickness = 2
            space_counter += 1
        else:
            color = (0, 0, 255)
            thickness = 1
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
    cvzone.putTextRect(img, f'Free: {space_counter}/{len(position_list)}', (20, 40), scale=2, thickness=3, offset=5, colorR=(0, 200, 0))
            

while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, img = cap.read()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (3, 3), 1)
    img_threshold = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    img_median = cv2.medianBlur(img_threshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    img_dilate = cv2.dilate(img_median, kernel, iterations=1)

    check_spaces(img_dilate)
    cv2.imshow("image", img)
    # cv2.imshow("image_blur", img_blur)
    # cv2.imshow("image_threshold", img_threshold)
    cv2.waitKey(20)
