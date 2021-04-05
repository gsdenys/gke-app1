from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")

@app.route('/')
def hello_world():
    return 'Applocation 1'

if __name__ == "__main__":
	app.run()
