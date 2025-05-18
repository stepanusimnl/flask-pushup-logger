# __init__ yang pertama kali dijalankan flask
# set environment var FLASK_APP untuk WSGI sehingga aplikasi dapat berjalan
# export/set FLASK_APP=folder(__init__.py) or file.py
# flask run

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

# create app
def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' # jika belum login
    login_manager.init_app(app)

    # find specific user from id in session cookie
    # setiap halaman load, load_user dipanggil
    # hasilnya disimpan pada current_user
    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Blueprint untuk organize files pada flask project
    from .main import main as main_blueprint # import Blueprint
    app.register_blueprint(main_blueprint)

    from.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app