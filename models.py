from . import db

# create database cli
# from pushup_logger import db, create_app

# app = create_app()

# with app.app_context():
#     db.create_all()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))