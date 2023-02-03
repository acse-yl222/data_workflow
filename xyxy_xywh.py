import numpy as np
import cv2


def xyxy2xywh(bbox, image_shape):
    new_bbox = np.zeros_like(bbox)
    new_bbox[:, 2] = np.absolute(bbox[:, 0] - bbox[:, 2]) / image_shape[1]
    new_bbox[:, 3] = np.absolute(bbox[:, 1] - bbox[:, 3]) / image_shape[0]
    new_bbox[:, 0] = (bbox[:, 0] + bbox[:, 2]) / (2 * image_shape[1])
    new_bbox[:, 1] = (bbox[:, 1] + bbox[:, 3]) / (2 * image_shape[0])
    return new_bbox

def xywh2xyxy(boxes):
    newboxes = np.zeros_like(boxes)
    newboxes[:, 0] = boxes[:, 0] - boxes[:, 2] // 2
    newboxes[:, 1] = boxes[:, 1] - boxes[:, 3] // 2
    newboxes[:, 2] = boxes[:, 0] + boxes[:, 2] // 2
    newboxes[:, 3] = boxes[:, 1] + boxes[:, 3] // 2
    return newboxes


img = cv2.imread('moon_data/original_big_img/images/Lunar_A.jpg')
data = np.loadtxt('data/A.csv', delimiter=',', dtype=np.int)
data = data[:, :4]
for row in data:
    cv2.rectangle(img, (row[0], row[1]), (row[2], row[3]), (255,0,0))
# data = xyxy2xywh(data, img.shape)
# np.savetxt('Lunr_A.csv', data,delimiter=',')
cv2.imwrite('sample.png', img)