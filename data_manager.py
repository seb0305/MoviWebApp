from models import db, User, Movie

class DataManager():
    """
    DataManager for managing users and movies.

    Methods:
        get_users(): Returns all users.
        create_user(name): Creates a new user.
        get_movies(user_id): Returns all movies for a user.
        add_movie(movie): Adds a movie.
        delete_user(user_id): Deletes a user and their movies.
        update_movie(movie_id): Updates a movie.
        delete_movie(movie_id): Deletes a movie.
    """
    def get_users(self):
        """Returns all users."""
        return User.query.all()

    def create_user(self, name):
        """Creates a new user."""
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()

    def delete_user(self, user_id):
        """Deletes a user and their movies."""
        # Delete all movies for the user
        Movie.query.filter_by(user_id=user_id).delete()
        # Delete the user
        User.query.filter_by(id=user_id).delete()
        db.session.commit()

    def get_movies(self, user_id):
        """Returns all movies for a user."""
        return Movie.query.filter_by(user_id=user_id).all()

    def add_movie(self, movie):
        """Adds a movie."""
        db.session.add(movie)
        db.session.commit()

    def update_movie(self, movie_id, new_title):
        """Updates a movie."""
        movie = Movie.query.get(movie_id)
        if movie:
            movie.name = new_title
            db.session.commit()

    def delete_movie(self, movie_id):
        """Deletes a movie."""
        Movie.query.filter_by(id=movie_id).delete()
        db.session.commit()

