#!/usr/bin/env python3
""" Basic Babel setup """
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """  """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCAL = "en"
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@app.rout('/')
def index():
    return render_template('1-index.html')

if __name__=="__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
