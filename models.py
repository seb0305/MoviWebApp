from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """
    Represents a user in the database.

    Attributes:
        id (int): Primary key of the user.
        name (str): Name of the user.
        movies (list): List of movies associated with the user.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Movie(db.Model):
    """
    Represents a movie in the database.

    Attributes:
        id (int): Primary key of the movie.
        name (str): Name of the movie.
        director (str): Director of the movie.
        year (int): Release year of the movie.
        poster_url (str): URL of the movie poster.
        user_id (int): Foreign key to the user.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    director = db.Column(db.String(100))
    year = db.Column(db.Integer)
    poster_url = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('movies', lazy=True))
