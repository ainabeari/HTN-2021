from flask import Flask, redirect, url_for, render_template
import json

app = Flask(__name__)


@app.route("/")
def index(): #Main dashboard (for one user)
    return render_template("index.html")


@app.route("/challenges")
def challenges(): #Page 3 (current challenges)
    return render_template("challenges.html")




if __name__ == "__main__":
    app.run(debug=True)
