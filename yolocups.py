import os
from flask import Flask, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

'''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
'''

@app.route('/')
def yolocups():
	return render_template('index.html')

@app.route('/uploads', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		file = request.files['file']
		print "HELLO1"
		if file and allowed_file(file.filename) and file.filename.split('.')[-1] in app.config['ALLOWED_EXTENSIONS']:
			print "HELLO4"
			filename = secure_filename(file.filename)
			print "HELLO"
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			print "HELLO2"
			return redirect(url_for('upload_file',filename=filename))
	return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
'''

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