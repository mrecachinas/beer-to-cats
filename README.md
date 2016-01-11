#Beer to Cats#

##Installation##
1. Ensure that you have python 2.7.5+
2. Install [pip](http://www.pip-installer.org/en/latest/installing.html)
    - On Ubuntu: `sudo apt-get install python-pip`
    - On Windows, OS X, or Ubuntu: 
        1. First, download [get-pip.py](https://raw.github.com/pypa/pip/master/contrib/get-pip.py) `$ curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py`
        2. Then run `$ python get-pip.py`
3. `$ pip install -r requirements.txt` (may require `sudo`)

###Installation Errors?###

We did not experience any issues installing natively. We did experience issues installing PIL on 

##Usage##
There are two primary ways to use the project:

1. Run the program via the command line and input images as command line parameters.
    ```
    $ python beer_to_cats.py <image.{png,jpg,jpeg,gif}>
    ```

2. Run the program on the webapp we've created. You can do that ~~either by navigating to [BeerToCats.com](http://www.BeerToCats.com)~~ (Edit: we've been having issues with pip and Heroku, so we're currently moving to an EC2 instance) by executing the following commands:
    ```
    $ python yolocups.py
     * Running on http://127.0.0.1:5000/
     * Restarting with reloader
    ```
Then navigate to http://127.0.0.1:5000/ and follow the instructions on the website as you would otherwise.

##Demo##
####Input:####

![IceCream](test/anat-ice-cream.jpg)

####Output:####

![Covered](test/anat-ice-cream-out.jpg)

####Input:####

![solo](example_pics/Cup.jpg)

####Output:####

![solo-out](uploads/test-Cup.jpg)

##Theory##
Let's say we have the following image where we want to find all of the solo cups and cover them with a cat. We will refer to this image in the following paragraphs.

![IceCream](test/anat-ice-cream.jpg)

There are several widely-used methods for feature detection – e.g. [Haar-like Feature Detection](https://www.cs.cmu.edu/~efros/courses/LBMV07/Papers/viola-cvpr-01.pdf), [Histogram-of-Oriented Gradient (HOG) Feature Detection](http://lear.inrialpes.fr/people/triggs/pubs/Dalal-cvpr05.pdf), etc.

For this project, we chose HOG detection. Therefore, we also needed to use a [Support Vector Machine (SVM)](http://en.wikipedia.org/wiki/Support_vector_machine) as the classifier.

To get the best results, we need a training set. We peroused the web for images of cans, bottles, and solo cups. Then, since this involves supervised learning, we went through drawing boxes around all of the cans, bottles, and cups. Using the previous image, we end up with the following:

![IceCreamBox](test/anat-ice-cream-annot.jpg)

Once we have a good set of these, we generate an XML file of these images with the box annotations. From this, we then compute the HOG representation of the boxed images. We'll choose the most prominent solo cup for this example.

Before HOG:

![SoloCup](test/solo.png)

How the computer sees it:

![SoloCup](test/solo-computer.jpg)

After computing the HOG of the image:

- Overlayed HOG Representation (computed using Mathematica)

![SoloCupComputer](test/solo-visible-gradient.png)

- Pure HOG Representation (computed using Matlab)

![SoloCupHog](test/solo-hog.png)

- Another Pure HOG Representation (using [MIT's HOGgles](http://web.mit.edu/vondrick/ihog/))

![SoloCupHog](test/solo-hog-mit.jpg)



These are fed into the SVM, with all of the possible orientations replicated and fed into the SVM as well.

###OK, so What is Histogram of Oriented Gradient (HOG)?###

The essence of HOG, or any feature descriptors for computer vision revolves around the fact that we want the computer to understand what the object it's looking at. HOG relies on the fact that the local object will be composed of pixels with similar values while the background will be composed of contrasting pixels. Thus, based on these differences in neighboring pixel values, we can determine the edge orientation of a particular pixel. The combination of all these histograms represent the actual features.

###What's a Support Vector Machine (SVM)?###

A support vector machine is a common, yet robust, supervised learning classifier. The idea of supervised learning is that given a training data points each belonging to a particular category, we use a supervised learning model like Support Vector Machine, Logistic Regression, Naïve-Bayes, Neural Networks, Decision Trees, etc. to predict which category a new data point belongs to.

Support Vector Machines take a set of features and map it to a set of hyperplanes in some high dimensional space. This allows the model to have non-linearity. SVMS are used to maximize the margin of separation between classes. SVMs use a kernel function that is used to map the data points to fit the maximum-margin hyperplane. Depending on the data, we can use different kernel functions: [Wikipedia - Support Vector Machine](http://en.wikipedia.org/wiki/Support_vector_machine).

For our program, after we transform our image to get the HOG features, we take our window of mxn pixels and reshape it into 1x(mn). Each of the data points in the vector represents a pixel value, which represents a feature for our supervised learning model. The class of each data point is either 1 (for cup) or (-1) for non-cup. With these vectors as our training data, we run a support vector machine with linear kernel to create our model.

###Results###

In depth analysis of results coming soon.

###Future Improvements###
- Train with more images
- Compare with Haar-like feature detection
- Use neural nets for a deeper learning

##TODO##
For program:
- **Known Issue**: program only works currently on jpgs and NOT pngs.

For documentation:
- Edit `README.md`: ensure instructions actually work... ugh I hate instructions that don't work.
