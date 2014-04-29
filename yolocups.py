from flask import Flask, redirect, render_template, request
from werkzeug.utils import secure_filename

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

            return "Successfully uploaded " + str(filename)
    return ''


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