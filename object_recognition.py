import cv2 
import uuid
import os
import time
import tensorflow as tf

labels = ['thumbsup', 'thumbsdown', 'highfive', 'halfheart', 'fuckyou']
number_imgs = 5

IMAGES_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'collectedimages')
#print(IMAGES_PATH)

if not os.path.exists(IMAGES_PATH):
    if os.name == 'posix':
        os.makedirs(IMAGES_PATH)
    elif os.name == 'nt':
        os.makedirs(IMAGES_PATH)

for label in labels:
    path = os.path.join(IMAGES_PATH, label)
    if not os.path.exists(path):
        os.makedirs(path)




LABELIMG_PATH = os.path.join('Tensorflow', 'labelimg')

if not os.path.exists(LABELIMG_PATH):
    os.makedirs(LABELIMG_PATH)

#if os.name == 'posix': #mi ako nqmash windows, za momenta tupo za teb
    #!make qt5py3
if os.name =='nt':
    !cd {LABELIMG_PATH} && pyrcc5 -o libs/resources.py resources.qrc