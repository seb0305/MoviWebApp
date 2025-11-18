# MoviWebApp

A simple, production-ready Flask web application for managing movie collections. 
Features include user and movie creation, deletion, updating, and searching, with automatic fetching of movie details (including posters) from the OMDb API. 
The app includes clear error handling and a user-friendly interface for easy movie management.

## Features
- Add, view, update, and delete users.
- Add, view, update, and delete movies.
- Automatically fetch movie details (title, director, year, poster) from OMDb API.
- Delete users and movies with a trash bin icon.
- Error handling for common HTTP errors and exceptions.
- Responsive design with user-friendly UI.

## Installation
1. Clone the repository:
2. Create a virtual environment and activate it:
3. Install the required packages:
4. Set up your OMDb API key in config.py:
5. Run the application:

## Usage
- Visit `http://localhost:5000` to use the app.
- Add users and movies through the web interface.
- Delete users and movies using the trash bin icons.

## Configuration
- Store sensitive data like API keys in `config.py`.
- Add `.env` and `config.py` to `.gitignore` to keep your API keys secure.

## Documentation
- `app.py`: Main Flask application with routes and error handlers.
- `models.py`: Database models for users and movies.
- `data_manager.py`: Class for managing users and movies.
- `config.py`: Configuration settings and constants.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.