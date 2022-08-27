# the doc for Blueprint here:https://flask.palletsprojects.com/en/2.2.x/api/?highlight=blueprint#blueprint-objects
from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('login')
def login():
    # the doc for render_template is here https://flask.palletsprojects.com/en/2.2.x/api/?highlight=blueprint#template-rendering
    return render_template('login.html')


@ auth.route('logout')
def logout():
    return render_template('home.html')


@ auth.route('register')
def Register():
    return render_template('register.html')
