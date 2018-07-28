from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "This is not so secret, its just a demo!"

app.debug = True

toolbar = DebugToolbarExtension(app)

@app.route("/")
def index():
	return render_template("index.html")


app.run()