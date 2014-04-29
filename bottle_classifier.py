import dlib, sys, glob
from skimage import io

# cups_training = '/home/jyotiska/Dropbox/Computer Vision/cupdataset.xml'
bottle_training = '/home/jyotiska/Dropbox/Computer Vision/bottledataset.xml'
# bottle_test_dir = 'bottle_train'
options = dlib.simple_object_detector_training_options()

options.add_left_right_image_flips = True

options.C = 4
options.epsilon = 0.01
options.num_threads = 8
options.be_verbose = True

dlib.train_simple_object_detector(bottle_training,"bottledetector.svm",options)

# print "\nTraining accuracy: ", dlib.test_simple_object_detector(cups_training,"cupdetector.svm")

