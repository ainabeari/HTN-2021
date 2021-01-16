from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/challenges")
def challenges():
    return render_template("challenges.html")


if __name__ == "__main__":
    app.run(debug=True)
