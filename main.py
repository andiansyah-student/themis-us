from flask import Flask, render_template, request, redirect, url_for
themisus = Flask(__name__)

@themisus.route('/')
def landing():
	return render_template('index.html')

if __name__ == '__main__':
	themisus.run()