from flask import Flask
from get_person_lambda import lambda_handler
from database_manager import update_databases_with_csv
import simplejson as json
import pprint

app = Flask(__name__)


def pretty_return(obj):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(json.dumps(obj))
    return obj

# setup routes


@app.route('/')
def index():
    resp = lambda_handler()
    return pretty_return(resp)


@app.route('/<person_id>')
def person(person_id):

    return pretty_return(lambda_handler(int(person_id)))


@app.route('/update-databases')
def update():

    obj = update_databases_with_csv()
    return pretty_return(obj)

if __name__ == "__main__":
    app.run(debug=True)
