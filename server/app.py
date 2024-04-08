# server/app.py
#!/usr/bin/env python3

from flask import Flask
from flask_migrate import Migrate

from .models import db, Employee, Onboarding, Review

# Create the Flask application instance
app = Flask(__name__)

# Configure the Flask app to use SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

# Create the Migrate instance and associate it with the Flask app and SQLAlchemy database
migrate = Migrate(app, db)

# Initialize the SQLAlchemy database with the Flask app
db.init_app(app)

# Run the Flask application if executed directly
if __name__ == "__main__":
    app.run(port=5555, debug=True)
