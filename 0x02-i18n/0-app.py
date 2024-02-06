#!/usr/bin/env python3
'''
This module is a flask application for a single route.
'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    The route to the home page of the app.
    """
    return render_template('index.html')
