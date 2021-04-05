import flask

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def health():
    return ""

@app.route('/app1', methods=['GET'])
def home():
    file = open('templates/index.html',mode='r')
 
    # read all lines at once
    all_of_it = file.read()
 
    # close the file
    file.close()

    return all_of_it #"<h1>Applocation 1!</h1>"

if __name__ == "__main__":
	app.run()
