import numpy as np
import cv2

label = 'moon_data/moon_yolo_v2/labels/A1248_A_0_1098.txt'
img = 'moon_data/moon_yolo_v2/images/A1248_A_0_1098.png'

img = cv2.imread(img)
bboxes = np.loadtxt(label, delimiter=' ')
bboxes = bboxes[:, 1:]


def get_box_corners(bbox: np.ndarray, width: int, height: int):
    """
    :param bbox: Series containing x, y, width, height description of bounding box (where (x, y) is the box center)
    :param width: Image width in pixels    :param height: Image height in pixels
    :return: Top-left and bottom-right points of bounding box as (x1, y2, x2, y2)    """
    top_left_x = int(bbox[0] * width) - (int(bbox[2] * width) // 2)
    top_left_y = int(bbox[1] * height) - (int(bbox[3] * height) // 2)
    bottom_right_x = top_left_x + int(bbox[2] * width)
    bottom_right_y = top_left_y + int(bbox[3] * height)
    return top_left_x, top_left_y, bottom_right_x, bottom_right_y


for bbox in bboxes:
    bbox = get_box_corners(bbox, 416, 416)
    start_point = (int(bbox[0]), int(bbox[1]))
    end_point = (int(bbox[2]), int(bbox[3]))
    img = cv2.rectangle(img, start_point, end_point, (255, 0, 0), 1)
cv2.imwrite('ok.png', img)
