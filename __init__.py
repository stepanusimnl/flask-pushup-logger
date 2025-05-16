# __init__ yang pertama kali dijalankan flask
# set environment var FLASK_APP untuk WSGI sehingga aplikasi dapat berjalan
# export/set FLASK_APP=folder(__init__.py) or file.py
# flask run

from flask import Flask


# create app
def create_app():
    app = Flask(__name__)

    # Blueprint untuk organize files pada flask project
    from .main import main as main_blueprint # import Blueprint
    app.register_blueprint(main_blueprint)

    from.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app