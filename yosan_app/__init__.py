from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('yosan_app.config')

db = SQLAlchemy(app)
from .models import employee

import yosan_app.views
