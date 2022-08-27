# the doc for Blueprint here:https://flask.palletsprojects.com/en/2.2.x/api/?highlight=blueprint#blueprint-objects
from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    # the doc for render_template is here https://flask.palletsprojects.com/en/2.2.x/api/?highlight=blueprint#template-rendering
    return render_template("home.html")
