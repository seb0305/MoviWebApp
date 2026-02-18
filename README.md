# MoviWebApp
**Flask Movie Collection Manager with OMDb API Integration, Posters & Full CRUD Operations**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-blue)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-green)](https://www.sqlite.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-orange)](https://www.sqlalchemy.org/)
[![OMDb](https://img.shields.io/badge/OMDb-API-red)](https://www.omdbapi.com/)

## 🎯 Features

| Feature | Description |
|---------|-------------|
| **User Management** | Add/delete users (auto-cascades movies) |
| **Movie Collections** | Per-user movies with title, director, year, posters |
| **OMDb Auto-Fetch** | Enter title → Instant details/poster from OMDb API |
| **Full CRUD** | Create/update/delete movies per user |
| **Trash Bin UI** | Intuitive delete buttons with confirmation |
| **Error Handling** | 404/500 pages + exception logging |
| **Responsive Design** | Clean web interface for desktop/mobile |

## 🏗️ Tech Stack

**Backend:** Flask + Flask-SQLAlchemy + SQLite (`data/movies.db`)  
**Data:** DataManager class + User/Movie models  
**API:** OMDb (title → title/director/year/poster)  
**Config:** `.env` + `config.py` for API keys  
**Deployment:** Render/Heroku/PythonAnywhere ready

## 🚀 Quick Start

```bash
# Clone & setup
git clone <your-repo-url>
cd MoviWebApp

# Virtualenv & deps
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install flask flask-sqlalchemy python-dotenv requests

# Config OMDb key
echo "OMDB_API_KEY=your_key_here" > .env

# Run
python app.py
# Visit http://localhost:5000
```

## 🎮 How to Use
1. Add Users

    Home → Enter name → Submit

2. Build Collections

    Click user → Add Movie → "The Matrix" → Auto-fetch details/poster!

3. Manage Movies

    Update titles → Delete with 🗑️ → Delete user (removes all movies)

Example: Add "Alice" → Add "Inception" → View Christopher Nolan poster → Delete!

## 🧠 Core Mechanics
- API Call: http://www.omdbapi.com/?t=Inception&apikey=KEY → Parse JSON

- Models: User(1-n)Movie (name, director, year, poster_url)

- Cascade Delete: User delete → All movies auto-purged

- DataManager: Centralized CRUD (get/create/update/delete)

## 📊 Database Schema
```text
erDiagram
    User {
        int id PK
        string name
    }
    Movie {
        int id PK
        string name
        string director
        int year
        string poster_url
        int user_id FK
    }
    User ||--o{ Movie : "owns"
```

## 📝 Development
```bash
# Debug mode
export FLASK_ENV=development
python app.py

# Shell access
flask shell
>>> from data_manager import DataManager; dm = DataManager()

# Test OMDb
curl "http://www.omdbapi.com/?t=Matrix&apikey=sk..."
```
## 🙌 Contributing
- Fork → Add features (ratings, search)

- Test full CRUD + OMDb flow

- PR with failing tests fixed!


## 📄 License
MIT - Free for movie fans!