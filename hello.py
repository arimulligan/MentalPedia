# imports flask, a function which can redirect the current url
# to a different one, and url_for (idk what that is yet)
from flask import Flask, redirect, url_for, render_template, request, session, flash
import copy

# creating the app
app = Flask(__name__)
app.secret_key = "aC@nth8scdjkfdhfjdsfkdksm12345678910helloworlddlrowolleh"

# when you click on the link, it directs to this page
@app.route("/")
def home():
    # index = open("templates/index.html").read().format(message=["Anxiety", "Burn Out", "Stress"])
    return render_template("index.html")

@app.route("/home")
def tohome():
    return redirect(url_for("home"))

@app.route("/search")
def search():
    return render_template("search.html")

firstpage_questions = {
 #format is 'question':[options]
    'In the last month, how often have you sat down and properly relaxed? '
    'Choose 1 for once, and 10 for I relax all the time.': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
    'Have you eaten more/less in the past month? From one to ten how much have your eating habits changed?': ['1', '2', '3',
                                                                                                              '4', '5', '6',
                                                                                                              '7', '8', '9',
                                                                                                              '10'],
    'Over the past month, have you been procrastinating more than ever? 1 for nope, 10 for yes too much!': ['1', '2', '3',
                                                                                                            '4', '5', '6',
                                                                                                            '7', '8', '9',
                                                                                                            '10'],
    'Do you have perfectionistic tendencies? Do you strive to make your work the best?': ['Yes', 'No'],
    'In the past seven days, how many days have you been completely exhausted and lost all motivation?': ['1', '2', '3',
                                                                                                          '4', '5', '6',
                                                                                                          '7'],
    'How many days in the past week have you been having trouble staying or falling asleep?': ['1', '2', '3', '4', '5',
                                                                                               '6', '7'],
    'On a scale of one to ten how much do you worry or are nervous about an upcoming social situation?': ['1', '2', '3',
                                                                                                          '4', '5', '6',
                                                                                                          '7', '8', '9',
                                                                                                          '10'],
    'How many days in the past two weeks does your heart race randomly?': ["not at all", "several days",
                                                                           "more than half the days",
                                                                           "nearly every day"],
    'How many times a day do you get easily irritated by other people/things? From 1 to 10.': ['1', '2', '3', '4', '5',
                                                                                               '6', '7', '8', '9', '10'],
    'Have you felt ‘on edge’ or unsettled in the past month?': ['Not at all', 'A few times a week', 'Every day',
                                                                'All the time every day'],
    'Do you feel like you’ve been on ‘low power mode’ in the last two weeks?': ["not at all", "several days",
                                                                                "more than half the days",
                                                                                "nearly every day"],
    'In the past month, have you noticed digestive issues, such as diarrhoea and constipation? '
    '1 being nope, and 10 being yes my bowels have been so bad recently.': ['1', '2', '3', '4', '5', '6', '7', '8', '9',
                                                                            '10'],
    'From one to ten, how many extra pimples – apart from the pimples that usually come up '
    '(like the ones when you’re on your period or eating unhealthy) – have formed over the past week?': ['1', '2', '3',
                                                                                                          '4', '5', '6',
                                                                                                          '7', '8', '9',
                                                                                                          '10'],
    'Have you ever caught yourself clenching your jaw or grinding your teeth in the past month?': ['No??',
                                                                                                   'Very rarely',
                                                                                                   'Sometimes',
                                                                                                   'A few times a week',
                                                                                                   'Several times a day'
                                                                                                   ],
    'Have you bitten your nails, fidgeted with your phone, '
    'or showed any nervous behaviours more frequently in the past two weeks?': ['Not at all', 'Several days',
                                                                                'More than half the days',
                                                                                'Nearly every day']
}


@app.route("/takethetest", methods=["POST", "GET"])
def first_page():
    questions = copy.deepcopy(firstpage_questions)
    return render_template('takethetest.html', o=questions)


def test():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("takethetest"))
    else:
        if "user" in session:
            return redirect(url_for("takethetest"))
        return render_template("takethetest.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

# runs the app, and debug=true means that it reloads the page without
# having to load it on this virtual environment


if __name__ == "__main__":
    app.run(debug=True)

# something that says "hello" to the name of the url
# @app.route("/<name>")
# def user(name):
#     return f"Hello {name}!"
# redirects page to homepage
# @app.route("/admin/")
# def admin():
#     return redirect(url_for("user", name="Admin!"))
