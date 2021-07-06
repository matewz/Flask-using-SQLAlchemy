from flask import Flask, render_template
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///system.db'
db = SQLAlchemy(app)


import json
import sqlite3


# Select All
# Select One
# Add
# Update
# Delete

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150))
    address = db.Column(db.String(150))


@app.route('/', methods=['GET'])
def index_html():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    print("Server running")
