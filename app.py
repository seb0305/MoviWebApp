from flask import Flask
from data_manager import DataManager
from models import db, Movie
import os

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

@app.route('/')
def home():
    return "Welcome to MoviWeb App!"

@app.route('/users')
def list_users():
    users = data_manager.get_users()
    return str(users)  # Temporarily returning users as a string

# Create the database tables if they don't exist
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
