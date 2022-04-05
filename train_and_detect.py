import os
import wget
import object_detection
import matplotlib
import tensorflow as tf
print(tf.version.VERSION)

CUSTOM_MODEL_NAME = 'my_ssd_mobnet' 
PRETRAINED_MODEL_NAME = 'ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8'
PRETRAINED_MODEL_URL = 'http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8.tar.gz'
TF_RECORD_SCRIPT_NAME = 'generate_tfrecord.py'
LABEL_MAP_NAME = 'label_map.pbtxt'

paths = {
    'WORKSPACE_PATH': os.path.join('Tensorflow', 'workspace'),
    'SCRIPTS_PATH': os.path.join('Tensorflow','scripts'),
    'APIMODEL_PATH': os.path.join('Tensorflow','models'),
    'ANNOTATION_PATH': os.path.join('Tensorflow', 'workspace','annotations'),
    'IMAGE_PATH': os.path.join('Tensorflow', 'workspace','images'),
    'MODEL_PATH': os.path.join('Tensorflow', 'workspace','models'),
    'PRETRAINED_MODEL_PATH': os.path.join('Tensorflow', 'workspace','pre-trained-models'),
    'CHECKPOINT_PATH': os.path.join('Tensorflow', 'workspace','models',CUSTOM_MODEL_NAME), 
    'OUTPUT_PATH': os.path.join('Tensorflow', 'workspace','models',CUSTOM_MODEL_NAME, 'export'), 
    'TFJS_PATH':os.path.join('Tensorflow', 'workspace','models',CUSTOM_MODEL_NAME, 'tfjsexport'), 
    'TFLITE_PATH':os.path.join('Tensorflow', 'workspace','models',CUSTOM_MODEL_NAME, 'tfliteexport'), 
    'PROTOC_PATH':os.path.join('Tensorflow','protoc')
 }

files = {
    'PIPELINE_CONFIG':os.path.join('Tensorflow', 'workspace','models', CUSTOM_MODEL_NAME, 'pipeline.config'),
    'TF_RECORD_SCRIPT': os.path.join(paths['SCRIPTS_PATH'], TF_RECORD_SCRIPT_NAME), 
    'LABELMAP': os.path.join(paths['ANNOTATION_PATH'], LABEL_MAP_NAME)
}

for path in paths.values():
    if not os.path.exists(path):   
            if os.name == 'posix':
                os.makedirs(path)
            elif os.name == 'nt':
                 os.makedirs(path)

os.environ['PATH'] += os.pathsep + os.path.abspath(os.path.join(paths['PROTOC_PATH'], 'bin'))

#VERIFICATION_SCRIPT = os.path.join('Tensorflow\models', 'research', 'object_detection', 'builders', 'model_builder_tf2_test.py')
#print(VERIFICATION_SCRIPT)
'''labels = [{'name':'ThumbsUp', 'id':1}, {'name':'ThumbsDown', 'id':2}, {'name':'HighFive', 'id':3}, {'name':'HalfHeart', 'id':4}, {'name':'FuckYou', 'id':5},]

with open(files['LABELMAP'], 'w') as f:
    for label in labels:
        f.write('item { \n')
        f.write('\tname:\'{}\'\n'.format(label['name']))
        f.write('\tid:{}\n'.format(label['id']))
        f.write('}\n')

#print('1  ', files['TF_RECORD_SCRIPT'], '\n')
#print('2  ',paths['IMAGE_PATH'], '\n')
#os.path.join(paths['IMAGE_PATH'], 'train')
#print('3  ',paths['IMAGE_PATH'], '\n')
#print('4  ',files['LABELMAP'])


#print('5  ',paths['ANNOTATION_PATH'])
#os.path.join(paths['ANNOTATION_PATH'], 'train.record')
#print('6  ',paths['ANNOTATION_PATH'])

#python Tensorflow\scripts\generate_tfrecord.py -x Tensorflow\workspace\images -l Tensorflow\workspace\annotations\label_map.pbtxt -o Tensorflow\workspace\annotations 
#!python Tensorflow\scripts\generate_tfrecord.py -x {os.path.join(paths['IMAGE_PATH'], 'test')} -l {files['LABELMAP']} -o {os.path.join(paths['ANNOTATION_PATH'], 'test.record')} 

#!python Tensorflow\scripts\generate_tfrecord.py -x {os.path.join(Tensorflow\workspace\images, 'train')} -l Tensorflow\workspace\annotations -o {os.path.join(Tensorflow\workspace\annotations, 'train.record')} 

#python Tensorflow\scripts\generate_tfrecord.py -x os.path.join(Tensorflow\workspace\images, 'train') -l Tensorflow\workspace\annotations\label_map.pbtxt -o os.path.join(Tensorflow\workspace\annotations, 'train.record') '''
