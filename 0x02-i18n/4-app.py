#!/usr/bin/env python3
'''
This module is a flask application for a single route.
'''
from flask import Flask, render_template, request
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


@babel.localeselector
def get_locale() -> str:
    """
    A function to return the prefered language based on the
    request of the user.
    """
    locale = request.args.get('locale')
    if locale:
        if locale in app.config['LANGUAGES']:
            return locale

        # locale can be this formate [fr|en], so split it to get the
        # preferred
        if '[' in locale:
            locale = locale.strip('[]').split('|')
        for locs in locale:
            if locs in app.config['LANGUAGES']:
                return locs

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    The route to the home page of the app.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
