import flask

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def health():
    return ""

@app.route('/app1', methods=['GET'])
def home():
    return "<h1>Applocation 1!</h1>"

if __name__ == "__main__":
	app.run()
