from . import db
from flask_login import UserMixin # objek user punya is_authenticated, is_active, is_anonymus, get_id()
from datetime import datetime

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
    # 1 user punya banyak workout
    # backref agar bisa mengakses dari Workout ke User menggunakan .author
    workouts = db.relationship('Workout', backref='author', lazy=True)

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pushups = db.Column(db.Integer, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)
    comment = db.Column(db.Text, nullable=False)
    # setiap workout (pushup) dimiliki oleh 1 user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)