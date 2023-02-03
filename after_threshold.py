import os
import cv2

import numpy as np

def xyxy2xywh(bbox,image_shape):
    new_bbox = np.zeros_like(bbox)
    new_bbox[:, 2] = np.absolute(bbox[:, 0] - bbox[:, 2]) / image_shape[1]
    new_bbox[:, 3] = np.absolute(bbox[:, 1] - bbox[:, 3]) / image_shape[0]
    new_bbox[:, 0] = (bbox[:, 0] + bbox[:, 2]) / (2 * image_shape[1])
    new_bbox[:, 1] = (bbox[:, 1] + bbox[:, 3]) / (2 * image_shape[0])
    return new_bbox


def flit_small_big_bounding_bboxes(data):
    w = data[:, 0] - data[:, 2]
    h = data[:, 1] - data[:, 3]
    size = np.sqrt(w * h)
    index = size > 8
    return data[index]


def resize_img_bbox(img, bbox, base_size_w, base_size_h):
    img_shape = img.shape
    img = cv2.resize(img, (base_size_h, base_size_w))
    scale_h = base_size_h / img_shape[0]
    scale_w = base_size_w / img_shape[1]
    bbox[:, 0], bbox[:, 2] = bbox[:, 0] * scale_w, bbox[:, 2] * scale_w
    bbox[:, 1], bbox[:, 3] = bbox[:, 1] * scale_h, bbox[:, 3] * scale_h
    bbox = flit_small_big_bounding_bboxes(bbox)
    bbox = xyxy2xywh(bbox,(416,416))
    return img, bbox


dir_list = ['A1248','A11232', 'A3744', 'B1248','B11232', 'B3744', 'C1248','C11232', 'C3744','D1248', 'D11232', 'D3744']
for index, dir in enumerate(dir_list):
    print(index)
    new_dir = os.listdir(os.path.join('data', dir))
    for file in new_dir:
        if '.png' in file:
            img = cv2.imread(os.path.join(os.path.join('data', dir), file))
            bbox = np.loadtxt(os.path.join(os.path.join('data', dir), file.replace('.png', '.txt')), delimiter=',')[:,
                   :4]
            img, bbox = resize_img_bbox(img, bbox, 416, 416)
            new_bbox = np.zeros((len(bbox), 5))
            new_bbox[:, 1:] = bbox
            new_img_name = dir + '_' + file
            new_bbox_name = dir + '_' + file.replace('.png', '.txt')
            new_path_img = os.path.join('moon_data/moon_yolo_v2/images', new_img_name)
            new_path_bbox = os.path.join('moon_data/moon_yolo_v2/labels', new_bbox_name)
            cv2.imwrite(new_path_img, img)
            np.savetxt(new_path_bbox, new_bbox, delimiter=' ', fmt='%.4e')
