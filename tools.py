import os
import shutil


def create_data_for_json(path):
    path_list = ['train', 'val', 'test']
    for i in path_list:
        try:
            os.makedirs(os.path.join(path, i, 'images'))
        except:
            pass
        try:
            os.makedirs(os.path.join(path, i, 'labels'))
        except:
            pass
    for i in path_list:
        for index, image in enumerate(os.listdir(os.path.join(path, 'images', i))):
            shutil.copy(os.path.join(path, 'images', i, image), os.path.join(path, i, 'images', image))
            print(index)
        for index, label in enumerate(os.listdir(os.path.join(path, 'labels', i))):
            shutil.copy(os.path.join(path, 'labels', i, label), os.path.join(path, i, 'labels', label))
            print(index)

#create_data_for_json('moon_data/moon_yolo_teacher/yolo')


def make_json_file(path):
    path_list = ['train', 'val', 'test']
    for i in path_list:
        os.system("python yolo2coco.py "+os.path.join(path,i))

#make_json_file('moon_data/moon_yolo_teacher/yolo')

def move_files(origianl_path,path):
    path_list = ['train', 'val', 'test']
    for i in path_list:
        shutil.copy(os.path.join(origianl_path,i,'annotations/result.json'),os.path.join(path,'instances_'+i+'2017.json'))

move_files('moon_data/moon_yolo_teacher/yolo','moon_data/moon_yolo_teacher/coco/annotations')

def move_img_label(path,new_path):
    dir_list = os.listdir(path)
    for dir in dir_list:
        file_list = os.listdir(os.path.join(path, dir))
        for file in file_list:
            if '.png' in file:
                shutil.copyfile(os.path.join(path, dir, file),
                                os.path.join('new_moon_data', 'images', file))
                shutil.copyfile(os.path.join('original_moon_data', dir, file.replace('.png', '.txt')),
                                os.path.join('new_moon_data', 'labels', file.replace('.png', '.txt')))