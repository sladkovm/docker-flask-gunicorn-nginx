from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')
#
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/test'
# db = SQLAlchemy(app)
#
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(120), unique=True)
#
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#
#     def __repr__(self):
#         return '<User {}>'.format(self.username)


@app.route("/")
def api_endpoint():
    return "This is API endpoint"


@app.route("/resource")
def api_resource():
    return "This is API resource"



if __name__ == '__main__':
    app.run(debug=True)

