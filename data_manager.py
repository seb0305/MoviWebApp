from models import db, User, Movie

class DataManager():
    def create_user(self, name):
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()

    def get_users(self):
        return User.query.all()

    def delete_user(self, user_id):
        # Delete all movies for the user
        Movie.query.filter_by(user_id=user_id).delete()
        # Delete the user
        User.query.filter_by(id=user_id).delete()
        db.session.commit()

    def get_movies(self, user_id):
        return Movie.query.filter_by(user_id=user_id).all()

    def add_movie(self, movie):
        db.session.add(movie)
        db.session.commit()

    def update_movie(self, movie_id, new_title):
        movie = Movie.query.get(movie_id)
        if movie:
            movie.name = new_title
            db.session.commit()

    def delete_movie(self, movie_id):
        Movie.query.filter_by(id=movie_id).delete()
        db.session.commit()

