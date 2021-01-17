from flask import Flask, redirect, url_for, render_template, request
import json

app = Flask(__name__)
# Reading User Data
ArielleDir = 'C:\\Users\\Arielle\\Documents\\GitHub\\HTN-2021\\data\\user_data.json'
AllenDir = 'C:\\Users\\Allen\\Documents\\GitHub\\HTN-2021\\data\\user_data.json'
with open(ArielleDir, "r") as read_file:
    data = json.load(read_file)  # dictionary type

# Assigning variables for the user
# name = data.get("name") --> do this to get value of a key can use lists as well

# for key, value in data.items():
#    print(data.get(key))#list(data.get(key).items())


@app.route("/")
def index():  # Main dashboard (for one user)
    # Some examples of getting some key data
    name = data.get("users").get("user1").get("name")
    challenges = list(data.get("users").get("user1").get("challenges"))
    return render_template("index.html", content=name)


@app.route("/challenges")
def challenges():  # Page 3 (current challenges)
    #def button():
     #   print("Hello World")
    return render_template("challenges.html")


@app.route("/new-challenge", methods=("GET", "POST"))
def create_challenges():  # Page 3 (create new challenge)
    if request.method == 'POST':
        title = request.form['title']
        fruit = request.form['fruit']
        print(title)
        print(fruit)
    return render_template("create-challenge.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
