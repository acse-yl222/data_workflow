import numpy as np
import pandas as pd
import cv2
import os
def read_file(path):
    a = pd.read_csv(path,delimiter=' ',header=None,index_col=None)
    return np.array(a,dtype=np.float64)

def xyxy2xywh(bbox,image_shape):
    new_bbox = np.zeros_like(bbox)
    new_bbox[:, 2] = np.absolute(bbox[:, 0] - bbox[:, 2]) / image_shape[1]
    new_bbox[:, 3] = np.absolute(bbox[:, 1] - bbox[:, 3]) / image_shape[0]
    new_bbox[:, 0] = (bbox[:, 0] + bbox[:, 2]) / (2 * image_shape[1])
    new_bbox[:, 1] = (bbox[:, 1] + bbox[:, 3]) / (2 * image_shape[0])
    return new_bbox

file_list = os.listdir('new_moon_data/labels')

for file in file_list:
    original_bbox = read_file(os.path.join('new_moon_data/labels',file))
    img = cv2.imread(os.path.join('new_moon_data/images',file.replace('.txt','.png')))
    new_bbox = np.zeros_like(original_bbox)
    ok = xyxy2xywh(original_bbox[:,1:],img.shape)
    new_bbox[:,1:] = ok
    np.savetxt(os.path.join('new_moon_data','new_label',file), new_bbox, fmt="%.3f", delimiter=' ')