import flask
# import the library

app = flask.Flask(__name__)
app.config["DEBUG"] = True
# starts the debugger instead of generic error message in the browser


@app.route('/', methods=['GET'])
# maps the url and the allowed methods to the specified function
def home():
    return "<h1>From Gem Mining to Snake Charming</h1><p>First foray into building something with Python. If Sinatra is to Flask then 'Sinatra doesn't know this ditty' will be...</p>"


app.run()
# method for running the application server
