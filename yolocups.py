import os
from flask import Flask, redirect
from flask import render_template

app = Flask(__name__)

@app.route('/')
def yolocups():
	return render_template('index.html')

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