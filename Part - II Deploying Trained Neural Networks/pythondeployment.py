import caffe
import cv2
import sys
import matplotlib.pyplot as plt
#import Image

def deploy(img_path):

    caffe.set_mode_gpu()
    MODEL_JOB_DIR = '/dli/data/digits/20180301-185638-e918'
    DATASET_JOB_DIR = '/dli/data/digits/20180222-165843-ada0'
    ARCHITECTURE = MODEL_JOB_DIR + '/deploy.prototxt'
    WEIGHTS = MODEL_JOB_DIR + '/snapshot_iter_735.caffemodel'
    
    # Initialize the Caffe model using the model trained in DIGITS.
    net = caffe.Classifier(ARCHITECTURE, WEIGHTS,
                           channel_swap=(2,1,0),
                           raw_scale=255,
                           image_d