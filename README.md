<h1>Beer to Cats</h1>

<h2>Installation</h2>
1. Ensure that you have python 2.7.5+
2. Install [pip](http://www.pip-installer.org/en/latest/installing.html)
    - On Ubuntu: `sudo apt-get install python-pip`
    - On Windows, OS X, or Ubuntu: 
        1. First, download [get-pip.py](https://raw.github.com/pypa/pip/master/contrib/get-pip.py)
        2. Then run `$ python get-pip.py`
3. `$ pip install -r requirements.txt` (may require `sudo`)

<h3>Errors</h3>
Try the [SimpleCV](https://github.com/sightmachine/simplecv#installation) github. They have a wealth of more in depth instructions for installation.

<h2>Usage</h2>
There are two primary ways to use the project:

1. Run the program via the command line and input images as command line parameters.
    ```
    $ python beer_to_cats.py <image.{png,jpg,jpeg,gif}> <optional threshold value>
    ```

2. Run the program on the webapp we've created. You can do that either by navigating to [Our Site](www.yolo.me) or executing the following commands:
    ```
    $ python yolocups.py
     * Running on http://127.0.0.1:5000/
     * Restarting with reloader
    ```
Then navigate to http://127.0.0.1:5000/ and follow the instructions on the website as you would otherwise.
