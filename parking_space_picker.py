import cv2
import pickle

img = cv2.imread('car_parking.jpg')
output = img.copy()

width, height = 40, 80


try: 
    with open('parking_position', 'rb') as f:
        position_list = pickle.load(f)
except:
    position_list = []


def mouse_click(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        position_list.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(position_list):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                position_list.pop(i)

    with open('parking_position', 'wb') as f:
        pickle.dump(position_list, f)


while True:
    img = cv2.imread('car_parking.jpg')
    output = img.copy()

    for pos in position_list:
        cv2.rectangle(output, pos, (pos[0] + width, pos[1] + height), (255, 0, 0), 2)

    cv2.imshow("image", output)
    cv2.setMouseCallback("image", mouse_click)
    cv2.waitKey(1)