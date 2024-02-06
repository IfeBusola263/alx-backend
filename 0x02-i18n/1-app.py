#!/usr/bin/env python3
'''
This module is a flask application for a single route.
'''
from flask import Flask, render_template
from flask_babel import Babel
from typing import List
app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    A configuration class to specify the languages for the app
    and other default configurations.
    """
    LANGUAGES: List[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = 'en'
    BABEL_DEFAULT_TIMEZONE: str = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index() -> str:
    """
    The route to the home page of the app.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
