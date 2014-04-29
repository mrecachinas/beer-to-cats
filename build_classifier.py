import dlib, sys, glob
from skimage import io

cups_training = '/home/jyotiska/Dropbox/Computer Vision/cupdataset.xml'
cups_training_2 = '/home/jyotiska/Dropbox/Computer Vision/cupdataset_3.xml'
cup_test_dir = 'Cups_train'
options = dlib.simple_object_detector_training_options()

options.add_left_right_image_flips = True

options.C = 4
options.epsilon = 0.01
options.num_threads = 8
options.be_verbose = True

dlib.train_simple_object_detector(cups_training_2,"cupdetector_3.svm",options)

# print "\nTraining accuracy: ", dlib.test_simple_object_detector(cups_training,"cupdetector.svm")


