from flask import Flask, redirect, url_for, render_template
import json
import numpy as np #for arrays

app = Flask(__name__)


@app.route("/")
def index(): #Main dashboard (for one user)
    #Reading User Data
    with open('C:\\Users\\Arielle\\Documents\\GitHub\\HTN-2021\\data\\user_data.json', "r") as read_file:
        data = json.load(read_file) #dictionary type

    #Assigning variables for the user
    name = data.get("name")
    challenges = list(data.get("challenges").keys()) #This is 1D list of challenges. There are currently two challenges:
    #challenge_1 = challenges[0] #This is the drinking water challenge
    #Going to reformat this in arrays so it's easy to access
    for key, value in data.items():
        print(data.get(key))#list(data.get(key).items())

    return render_template("index.html")


@app.route("/challenges")
def challenges(): #Page 3 (current challenges)
    return render_template("challenges.html")




if __name__ == "__main__":
    app.run(debug=True)
