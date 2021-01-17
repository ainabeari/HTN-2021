from flask import Flask, redirect, url_for, render_template, request
import json
#from google.cloud import firestore

# Initializing google cloud services
#import firebase_admin
#from firebase_admin import credentials
#from firebase_admin import firestore

# Use the application default credentials
#cred = credentials.ApplicationDefault()
# firebase_admin.initialize_app(cred, {
#    'traq-18583': project_id,
# }

#db = firestore.client()

#doc_ref = db.collection(u'users').document(u'alovelace')
# doc_ref.set({
#    u'first': u'Ada',
#    u'last': u'Lovelace',
#    u'born': 1815
# })

app = Flask(__name__)
# Reading User Data
ArielleDir = 'C:\\Users\\Arielle\\Documents\\GitHub\\HTN-2021\\data\\user_data.json'
AllenDir = 'C:\\Users\\Allen\\Documents\\GitHub\\HTN-2021\\data\\user_data.json'
with open(AllenDir, "r") as read_file:
    data = json.load(read_file)  # dictionary type

# Assigning variables for the user
# name = data.get("name") --> do this to get value of a key can use lists as well

# for key, value in data.items():
#    print(data.get(key))#list(data.get(key).items())


@app.route("/")
def index():  # Main dashboard (for one user)
    # Some examples of getting some key data
    return render_template("index.html", data=data)


@app.route("/challenges/<challenge_name>")
def challenges(challenge_name):  # Page 3 (current challenges)
    # def button():
    #   print("Hello World")
    return render_template("challenges.html", data=data)


@app.route("/new-challenge", methods=("GET", "POST"))
def create_challenges():  # Page 3 (create new challenge)
    if request.method == 'POST':
        challenge_name = request.form['challenge_name']
        print(challenge_name)
        return render_template("accountability.html", data=data)

        # start = request.form['start']
        # end = request.form['end']
        # task = request.form['task']  # This example only has one task
        # description = request.form['description']
        # type = request.form['type']
        # # Insert math for calculating the progress
        # length = 0
        #
        # # Updating json file (using example for user 2):
        # data.get('users').get('user2').get(
        #     'challenges').update({challenge_name: {}})
        # data.get('users').get('user2').get('challenges').get(
        #     challenge_name).update({"Tasks": {}})
        # data.get('users').get('user2').get('challenges').get(
        #     challenge_name).get("Tasks").update({"Task 1": {}})
        # # Add other stuff like description, how often after check with Allen:
        # data.get('users').get('user2').get('challenges').get(challenge_name).get(
        #     "Tasks").get("Task 1").update({"description": description})
        # data.get('users').get('user2').get('challenges').get(
        #     challenge_name).get("Tasks").get("Task 1").update({"type": type})
        # data.get('users').get('user2').get('challenges').get(challenge_name).get(
        #     "Tasks").get("Task 1").update({"complete": False})
        #
        # data.get('users').get('user2').get('challenges').get(
        #     challenge_name).get("Tasks").update({"Progress": {}})
        # data.get('users').get('user2').get('challenges').get(challenge_name).get(
        #     "Tasks").get("Progress").update({"total days": length})
        # data.get('users').get('user2').get('challenges').get(challenge_name).get(
        #     "Tasks").get("Progress").update({"current day": 0})
        # data.get('users').get('user2').get('challenges').get(
        #     challenge_name).get("Tasks").get("Progress").update({"progress": 0})

    return render_template("create-challenge.html", data=data)


@app.route("/accountability")
def accountability():  # Page 4 (new challenges - accountability)
    return render_template("accountability.html", data=data)


@app.route("/add-people")
def addPeople():  # Page 4 (new challenges - add people)
    return render_template("add-people.html")


@app.route("/home")
def home():  # Page 4 (new challenges - add people)
    return render_template("home.html")


@app.route("/onboarding")
def onboarding():  # Page 4 (new challenges - add people)
    return render_template("onboarding.html")


if __name__ == "__main__":
    app.run(debug=True)
