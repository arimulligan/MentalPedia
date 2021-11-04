# imports flask, a function which can redirect the current url
# to a different one, and url_for
from flask import Flask, redirect, url_for, render_template, request, session, flash
import copy
from flask_mail import Mail, Message

# creating the app
app = Flask(__name__)
app.secret_key = "aC@nth8scdjkfdhfjdsfkdksm12345678910helloworlddlrowolleh"


# when you click on the link, it directs to this page
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/home")
def tohome():
    return redirect(url_for("home"))


@app.route("/search")
def search():
    return render_template("search.html")


# makes a list of the questions
firstpage_questions = list()
with open("firstquestions.txt", "r") as file:
    for i in file:
        firstpage_questions.append(i.rstrip("\n"))

# converted two lists into a dictionary in the format 'question': ['num', 'num']
question_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
firstquestions_dict = {q: question_list for q in firstpage_questions}

# this deep copy is so if I make any changes to the duplicated list it won't affect the original list.
firstquestions = copy.deepcopy(firstquestions_dict)


# the request method means that if the sight reloads, the user still has their results saved
@app.route("/takethetest", methods=["POST", "GET"])
def takethetest():
    return render_template("takethetest.html", q=firstquestions)


# adding enumerate to this environment
@app.context_processor
def inject_enumerate():
    return dict(enumerate=enumerate)


#  this function calculates the percentage of burn out, stress and anxiety the user is experiencing in the past month
def calculate(firstq, lastq):
    mental_issue = 0
    for num in range(15):
        get_answers = list(firstquestions.keys())[num]
        answered = request.form.get(get_answers)
        if num >= firstq and num <= lastq:
            if num % 2 == 0:
                mental_issue += (int(answered) - 1) * 10 / 5
            elif num % 2 != 0:
                mental_issue += (10 - int(answered)) * 10 / 5
            else:
                continue
        else:
            continue
    return mental_issue



@app.route("/contact")
def contact():
    return render_template("contact.html")

# runs the app, and debug=true means that it reloads the page without
# having to load it on this virtual environment


if __name__ == "__main__":
    app.run(debug=True)


