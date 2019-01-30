import os

from flask import Flask


def create_app(test_config=None):
    # Create and configure Flaskr app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure instance folder actually exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # A simple page that says hello:

    @app.route('/hello/<var>')
    def hello(var):
        return "Hello there {}!".format(var)

    @app.route('/hell')
    def hell():
        return "Welcome to Hell!"

    from . import db
    db.init_app(app)

    return app
