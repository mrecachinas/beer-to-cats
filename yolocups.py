import os
from flask import Flask, redirect, render_template, request, url_for, send_from_directory
from werkzeug.utils import secure_filename
from PIL import Image
from skimage import io
from classify_func import classify

app = Flask(__name__)

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def yolocups():
    return render_template('index.html')


@app.route('/uploads', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']

        if file and allowed_file(file.filename) and file.filename.split('.')[-1] in app.config['ALLOWED_EXTENSIONS']:
            filename = secure_filename(file.filename)

            # Work with file here, redirect to a results page with processed image in template
            print "Hello"
            img = io.imread(file.stream)
            new_img = classify(img)
            new_img.save(app.config['UPLOAD_FOLDER']+"test-"+filename)
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename="test-"+filename))
    return 

@app.route('/show/<filename>')
def uploaded_file(filename):
    return render_template('classified.html', filename=filename)

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/demo')
def demo():
    return render_template('demo.html')


@app.route('/theory')
def theory():
    return render_template('theory.html')


@app.route('/yolo')
def yolo():
    return redirect("http://www.youtube.com/watch?v=z5Otla5157c", code=302)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html'), 404


if __name__ == '__main__':
    app.run(debug=True)