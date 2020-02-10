import flask
from flask import request, jsonify
# import the libraries needed

app = flask.Flask(__name__)
app.config["DEBUG"] = True
# starts the debugger instead of generic error message in the browser

pokemons = [
    {'id': 0,
     'name': 'Bulbasaur',
     'type': 'Grass',
     'generation': '1'},
    {'id': 1,
     'name': 'Charmander',
     'type': 'Fire',
     'generation': '1'},
    {'id': 2,
     'name': 'Squirtle',
     'type': 'Water',
     'generation': '1'}
]


@app.route('/', methods=['GET'])
# maps the url and the allowed methods to the specified function
# home page with a simple message
def home():
    return "<h1>From Gem Mining to Snake Charming</h1><p>First foray into building something with Python. If Sinatra is to Flask then 'Sinatra doesn't know this ditty' will be...</p>"


@app.route('/api/v1/resources/pokemons/all', methods=['GET'])
# returns all the pokemon available in our hard coded list
def api_all():
    return jsonify(pokemons)


@app.route('/api/v1/resources/pokemons', methods=['GET'])
# appends an integer as a query parameter to look for a specific pokemon from our list with a matching id
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id provided. Please specify an id."

    results = []

    for pokemon in pokemons:
        if pokemon['id'] == id:
            results.append(pokemon)

    return jsonify(results)


app.run()
# method for running the application server
