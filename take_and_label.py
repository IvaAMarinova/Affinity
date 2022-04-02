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

for label in labels:
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}\n'.format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        print('Collecting image {}\n'.format(imgnum))
        ret, frame = cap.read()
        imgname = os.path.join(IMAGES_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()


LABELIMG_PATH = os.path.join('Tensorflow', 'labelimg')

if not os.path.exists(LABELIMG_PATH):
    os.makedirs(LABELIMG_PATH)
#additional set up here in drive doc