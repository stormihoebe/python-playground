from flask import Flask
from get_person_lambda import lambda_handler
app = Flask(__name__)

@app.route('/')
def index():
    resp = lambda_handler()
    return resp


@app.route('/<person_id>')
def person(person_id):

    return lambda_handler(int(person_id))

if __name__ == "__main__":
    app.run(debug=True)