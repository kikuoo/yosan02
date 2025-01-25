from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///yosan_01.db"

db = SQLAlchemy(app)

from .models import employee


import yosan_app.views
