from flask import Flask
from flask import request, jsonify
from flask import render_template
# import the libraries needed

app = Flask(__name__)
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
def hello_world():
    return render_template("aloha_world.html")


@app.route('/home', methods=["GET"])
def home():
    return render_template('home.html')


@app.route('/about', methods=["GET"])
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')


@app.route('/api/v1/resources/pokemons/all', methods=['GET'])
# returns all the pokemon available in our hard coded list
def api_all():
    return app.send_static_file("data.json")


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
