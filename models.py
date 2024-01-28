from datetime import datetime

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    home_planet = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=False)
    image_url = db.Column(db.Text, default="/static/images/defaultuser.jpg")
    bio = db.Column(db.Text)

    @classmethod
    def signup(cls, username, email, password, home_planet, image_url):
        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = User(
            username=username,
            email=email,
            password=hashed_pwd,
            home_planet=home_planet,
            image_url=image_url,
        )

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):
        user = cls.query.filter_by(username=username).first()

        if user:
            is_auth = bcrypt.check_password_hash(user.password, password)
            if is_auth:
                return user
        return False

class Planet(db.Model):

    __tablename__ = "planets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    distance_from_sun = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    gravity = db.Column(db.Float)
    image_url = db.Column(db.Text)

class Airport(db.Model):

    __tablename__ = "airports"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    planet = db.Column(db.Integer, db.ForeignKey('planets.id'))


class Flight(db.Model):

    __tablename__ = "flights"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    departing_planet = db.Column(db.Integer, nullable=False)
    arriving_planet = db.Column(db.Integer, nullable=False)
    flight_time = db.Column(db.Float)


class Activity(db.Model):

    __tablename__ = "activities"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    description = db.Column(db.Text)
    planet = db.Column(db.Integer, db.ForeignKey('planets.id'))


class Hotel(db.Model):

    __tablename__ = "hotels"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    description = db.Column(db.Text)
    planet = db.Column(db.Integer, db.ForeignKey('planets.id'))


class Restaurant(db.Model):

    __tablename__ = "restaurants"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    description = db.Column(db.Text)
    planet = db.Column(db.Integer, db.ForeignKey('planets.id'))




def connect_db(app):
    """Connect to database."""
    app.app_context().push()
    db.app = app
    db.init_app(app)