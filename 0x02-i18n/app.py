#!/usr/bin/env python3
'''
This module is a flask application for a single route.
'''
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
from typing import List, Union, Dict
from pytz import timezone, exceptions
from datetime import datetime
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
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """
    A function to user login. the users dictionary is the
    dummy database used to validate a user login.
    """
    user_login = request.args.get('login_as')
    if user_login:
        return users[int(user_login)] if int(user_login) in users else None

    # the get method for a dict will return None if the attribute
    # is not found
    return user_login


@app.before_request
def before_request():
    """
    This function will execute before all other functions.
    specifically for user login.
    """
    user_info = get_user()
    g.user = user_info


@babel.localeselector
def get_locale() -> str:
    """
    A function to return the prefered language based on the
    request of the user.
    """
    default = request.accept_languages.best_match(app.config['LANGUAGES'])

    # Locale from URL parameters
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

    # Locale from user settings
    if g.user:
        locale = g.user.get('locale')
        if not locale:
            return default
        return locale if locale in app.config['LANGUAGES'] else default

    # Locale from request header
    locale = request.header.get('locale')
    if locale:
        return locale if locale in app.config['LANGUAGES'] else default

    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone() -> str:
    """
    This function gets the timezone of based on uRL parameter
    or the user setting or the default is used.
    """
    tz = request.args.get('timezone')
    if not tz and g.user:
        tz = g.user.get('timezone')

    if tz:
        try:
            tz_value = timezone(tz)
            return tz
        except exceptions.UnknownTimeZoneError as e:
            pass

    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index() -> str:
    """
    The route to the home page of the app.
    """
    if g.user:
        t = format_datetime(datetime.now())
        return render_template('index.html',
                               username=g.user.get('name'), ctime=t)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
