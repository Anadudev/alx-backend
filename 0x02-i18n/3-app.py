#!/usr/bin/env python3
""" Basic Babel setup """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """  """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCAL = "en"
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(["LANGUAGES"])

@app.route('/')
def index():
    return render_template('2-index.html')

if __name__=="__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
