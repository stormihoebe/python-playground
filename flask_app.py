from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from get_person_lambda import lambda_handler
app = Flask(__name__)

# setup database
app.config["SQLALCHEMY_DATABASE_URIi"] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key="True")
    name = db.Column(db.String(200))
    age = db.Column(db.Integer)

    def __repr__(self):
        return f"User('{self.id}', '{self.name}', '{self.age}')"

# setup routes


@app.route('/')
def index():
    resp = lambda_handler()
    return resp


@app.route('/<person_id>')
def person(person_id):

    return lambda_handler(int(person_id))

if __name__ == "__main__":
    app.run(debug=True)