from . import db
from flask_login import UserMixin # objek user punya is_authenticated, is_active, is_anonymus, get_id()

# create database cli
# from pushup_logger import db, create_app

# app = create_app()

# with app.app_context():
#     db.create_all()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))