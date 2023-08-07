import os

from flask import Flask, render_template, send_from_directory

root_dir = os.path.dirname(os.path.abspath(__file__))
static_directory = os.path.join(root_dir, "static")

app = Flask(__name__, template_folder=static_directory)


@app.route("/")
def index():
    return render_template("index.html")
	

@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory(static_directory, path)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
