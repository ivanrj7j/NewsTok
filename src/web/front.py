"""
Frontend for the website
"""
from flask import Blueprint, render_template

frontend = Blueprint("frontend", __name__)

@frontend.route('/')
def home():
    return render_template("index.html")