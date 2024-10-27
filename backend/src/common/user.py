from .database import get_db
from flask import Flask

app = Flask(__name__)
db = get_db(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
