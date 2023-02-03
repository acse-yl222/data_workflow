import mmcv
import os
import shutil
from argparse import ArgumentParser

import mmcv
import numpy
import numpy as np
from mmdet.apis import inference_detector, init_detector
import cv2
from mmyolo.registry import VISUALIZERS
from mmyolo.utils import register_all_modules, switch_to_deploy
import torch
from mmyolo.utils.labelme_utils import LabelmeFormat
from mmyolo.utils.misc import get_file_list, show_data_classes


config_file = 'model/config/yolov8_l.py'
checkpoint_file = 'model/weight/epoch_50.pth'
register_all_modules()
model = init_detector(config_file, checkpoint_file, device='cuda:0')


img = [np.zeros((416,416,3)) for i in range(10)]







