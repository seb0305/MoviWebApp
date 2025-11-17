from flask import Flask, render_template, request, redirect, url_for
from data_manager import DataManager
from models import db, Movie, User
import os
import requests

OMDB_API_KEY = '865834c6'  # Replace with your actual API key

app = Flask(__name__)

# Configure the database
basedir = os.path.abspath(os.path.dirname(__file__))
data_dir = os.path.join(basedir, 'data')
os.makedirs(data_dir, exist_ok=True)

app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data/movies.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)
data_manager = DataManager()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500


@app.route('/')
def index():
    users = data_manager.get_users()
    return render_template('index.html', users=users)

@app.route('/users', methods=['POST'])
def create_user():
    name = request.form['name']
    data_manager.create_user(name)
    return redirect(url_for('index'))

@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    data_manager.delete_user(user_id)
    return redirect(url_for('index'))


@app.route('/users/<int:user_id>/movies', methods=['GET'])
def get_movies(user_id):
    user = User.query.get(user_id)
    movies = data_manager.get_movies(user_id)
    return render_template('movies.html', movies=movies, user_id=user_id, user_name=user.name)

@app.route('/users/<int:user_id>/movies', methods=['POST'])
def add_movie(user_id):
    title = request.form['title']
    # Fetch movie data from OMDb
    response = requests.get(f'http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}')
    data = response.json()
    if data.get('Response') == 'True':
        movie = Movie(
            name=data['Title'],
            director=data['Director'],
            year=int(data['Year']),
            poster_url=data['Poster'],
            user_id=user_id
        )
        data_manager.add_movie(movie)
    return redirect(url_for('get_movies', user_id=user_id))


@app.route('/users/<int:user_id>/movies/<int:movie_id>/update', methods=['POST'])
def update_movie(user_id, movie_id):
    new_title = request.form['title']
    data_manager.update_movie(movie_id, new_title)
    return redirect(url_for('get_movies', user_id=user_id))

@app.route('/users/<int:user_id>/movies/<int:movie_id>/delete', methods=['POST'])
def delete_movie(user_id, movie_id):
    data_manager.delete_movie(movie_id)
    return redirect(url_for('get_movies', user_id=user_id))



# Create the database tables if they don't exist
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
