from flask import render_template
from . import main


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/temp')
def temp():
    return render_template('temp.html')


