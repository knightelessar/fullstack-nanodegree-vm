# install by the following
# pip3 install flask

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/db_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<User {self.id}, {self.name}>'


class Person(db.Model):
    __table_name__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Person id: {self.id}, name: {self.name}'

db.create_all()

@app.route('/')
def index():
    return 'Hello world!'

if __name__ == "__main__":
    app.run()

# run the flask app by executing the following in terminal
# FLASK_APP=flask-hello-app.py flask run
# FLASK_APP=flask-hello-app.py FLASK_DEBUG=true flask run

# or 
# python3 flask-hello-app.py
# FLASK_DEBUG=true python3 flask-hello-app.py