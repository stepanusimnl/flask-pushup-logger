# __init__ yang pertama kali dijalankan flask
# set environment var FLASK_APP untuk WSGI sehingga aplikasi dapat berjalan
# export/set FLASK_APP=folder(__init__.py) or file.py
# flask run

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# create app
def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)


    # Blueprint untuk organize files pada flask project
    from .main import main as main_blueprint # import Blueprint
    app.register_blueprint(main_blueprint)

    from.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app