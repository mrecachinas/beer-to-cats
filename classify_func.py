import os,sys,Image,dlib,random
from skimage import io
import numpy as np

# print "\nTest1 accuracy: ", dlib.test_simple_object_detector('/home/jyotiska/Dropbox/Computer Vision/cupdataset_2_test.xml',"cupdetector_2.svm")
# print "\nTraining accuracy: ", dlib.test_simple_object_detector('/home/jyotiska/Dropbox/Computer Vision/cupdataset_3.xml',"cupdetector_3.svm")

detector = dlib.simple_object_detector("cupdetector_4.svm")

# win_det = dlib.image_window()
# win_det.set_image(detector)

# win = dlib.image_window()
# test_dir = '/home/jyotiska/Dropbox/Computer Vision/Cups_test'
# convert_dir = '/home/jyotiska/Dropbox/Computer Vision/Cups_test_convert'
assorted_dir = 'ItemBucket/'

items =os.listdir(assorted_dir)

def classify(img):
  dets = detector(img)
  background = Image.fromarray(np.array(img))
  for d in dets:
    x = d.left()
    y = d.top()
    width = d.right() - x
    height = d.bottom() - y
    print ">> detection position left,top,right,bottom:", d.left(), d.top(), d.right(), d.bottom()

    r = random.randint(0,len(items)-1)
    random_item = Image.open(assorted_dir+"/"+items[r])
    
    resized = random_item.resize( (int(1.2*width),int(1.2*height)) )
    background.paste(resized, (d.left()-12,d.top()-10), resized)
  return background

if __name__ == '__main__':
  if len(sys.argv) != 2:
    print 'Usage: python '+sys.argv[0]+' <image.{png,jpg,jpeg,gif}>'
    sys.exit()
  in_image = sys.argv[1]
  in_img = io.imread(in_image)
  out_img = classify(in_img)
  out_img.save(in_image.split('.')[0]+'-out.jpg')
  out_img.show()
