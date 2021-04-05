import flask

app = flask.Flask(__name__)

# @app.route('/', methods=['GET'])
# def home():
#     return "Applocation 1"

@app.route('/app1', methods=['GET'])
def home1():
    return "<h1>Applocation 1!</h1>"

if __name__ == "__main__":
	app.run()
