# from flask import Flask

# app = Flask(__name__)

# # @app.route("/")
# # def home():
# #     return render_template("index.html")


import flask

app = flask.Flask(__name__)
#app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "Applocation 1"


if __name__ == "__main__":
	app.run()
