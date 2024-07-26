#!/usr/bin/env python3
"""_summary_

Returns:
    _type_: _description_
"""


from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """_summary_
    """

    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """_summary_

    Returns:
        str: _description_
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """_summary_

    Returns:
        str: _description_
    """
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run()
