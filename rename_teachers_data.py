import os
import shutil

import numpy as np

path = 'moon_teacher_original_training/Lunar_dataset_train'
new_path = 'moon_teacher_original_training/rename_imgs'

folds = ['images', 'labels']

images_list = os.listdir(os.path.join(path, folds[0]))
for index, image in enumerate(images_list):
    image_name = image
    text_name = image_name.replace('.jpg', '.txt')
    image_path = os.path.join(os.path.join(path, folds[0]), image_name)
    text_path = os.path.join(os.path.join(path, folds[1]), text_name)

    new_image_path = os.path.join(new_path, folds[0], str(index) + '.jpg')
    new_txt_path = os.path.join(new_path, folds[1], str(index) + '.txt')
    shutil.copy(image_path, new_image_path)
    shutil.copy(text_path, new_txt_path)
