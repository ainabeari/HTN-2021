from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def index():  # Main dashboard (for one user)
    return render_template("index.html")


@app.route("/challenges")
def challenges():  # Page 3 (current challenges)
    return render_template("challenges.html")


@app.route("/new-challenge")
def create_challenges():  # Page 3 (create new challenge)
    return render_template("create-challenge.html")


if __name__ == "__main__":
    app.run(debug=True)
