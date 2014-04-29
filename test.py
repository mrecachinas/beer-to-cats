import Image
import shutil
import dlib
import random
import os
import glob
from skimage import io

def classify(img):
    detector = dlib.simple_object_detector("cupdetector_2.svm")

    win_det = dlib.image_window()
    win_det.set_image(detector)

    win = dlib.image_window()
    test_dir = '/home/jyotiska/Dropbox/Computer Vision/Cups_test'
    convert_dir = '/home/jyotiska/Dropbox/Computer Vision/Cups_test_convert'
    assorted_dir = '/home/jyotiska/Dropbox/Computer Vision/Item bucket'

    items = os.listdir(assorted_dir)

    convert_i = 0
    for f in glob.glob(convert_dir+"/*.*"):
        print "processing file:", f
        img = io.imread(f)
        extension = f.split(".")[1]
        convert_file = "convert_"+str(convert_i)+"."+extension
        shutil.copy(f,convert_file)
        print "convert file:",convert_file
        background = Image.open(convert_file)
        dets = detector(img)

        print "number of cups detected:", len(dets)
        for d in dets:
        	x = d.left()
        	y = d.top()
        	width = d.right() - x
        	height = d.bottom() - y
            print "  detection position left,top,right,bottom:", d.left(), d.top(), d.right(), d.bottom()
            print width,height

            r = random.randint(0,len(items)-1)
            print r,items[r]
            random_item = Image.open(assorted_dir+"/"+items[r])
            # scale it a bit more, and adjust position

            # Apply blur?
            resized = random_item.resize( (int(1.2*width),int(1.2*height)) )
            background.paste(resized, (d.left()-12,d.top()-10), resized)

        background.show()
        background.save(convert_file)
        win.clear_overlay()
        win.set_image(img)
        win.add_overlay(dets)
        convert_i += 1

if __name__ == '__main__':
    classify()
