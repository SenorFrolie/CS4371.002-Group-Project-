"""
this is the server file that defines all our routes and how our website is going to work
"""
import flask
from flask import request
import random
from city_data import CityInfo
from state_data import StateData
import os
import flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    UserMixin,
    LoginManager,
    login_user,
    login_required,
    logout_user,
    current_user,
)

load_dotenv()

# app config stuff
app = flask.Flask(__name__)
app.secret_key = "secret"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db = SQLAlchemy(app)
app.config["TESTING"] = False

# login config stuff
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login_form"


class Person(UserMixin, db.Model):
    """
    this is the model of my users database
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        """
        idk just good to have
        """
        return "<User %r>" % self.username


with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    """
    returns the object of the user id turned in
    """

    return Person.query.get(int(user_id))


@app.before_first_request
def init_app():
    """
    making sure user is logged out just in case of cookies
    """

    logout_user()


@app.route("/")
def front_page():
    """
    this is the very first page that the user will see when the visit our site
    """

    return flask.render_template("front_page.html")


@app.route("/city_form", methods=["POST", "GET"])
def city_form():
    """
    this is the form that allows users to tell what information they want
    """

    return flask.render_template("city_form.html")


@app.route("/city_display", methods=["POST", "GET"])
def city_display():
    """
    this is the function that will display all the city information
    """

    city_name = request.form.get("city_name")
    city_object = CityInfo()
    city_object.get_info("Austin")

    return flask.render_template("city_display.html", city=city_name)


@app.route("/suggest_form", methods=["POST", "GET"])
def suggest_form():
    """
    this is the page where we will ask users their suggestions and retrieve their answers
    """

    return flask.render_template("suggest_form.html")


@app.route("/suggest_page", methods=["POST", "GET"])
def suggest_page():
    """
    this is the page that will show the users suggestions and prompt them if they want to do it again
    """

    drop_down_form = flask.request.form
    snow = drop_down_form["snow_answer"]
    rural = drop_down_form["rural_answer"]
    tax = drop_down_form["tax_answer"]
    rain = drop_down_form["rain_answer"]
    coast = drop_down_form["coast_answer"]
    income = drop_down_form["income_answer"]
    political = drop_down_form["political_answer"]
    university = drop_down_form["uni_answer"]
    mountain = drop_down_form["mountain_answer"]
    desert = drop_down_form["desert_answer"]
    population = drop_down_form["pop_answer"]
    waterfront = drop_down_form["water_answer"]
    home = drop_down_form["home_answer"]
    crime = drop_down_form["crime_answer"]

    # declaring points array and initializing
    points = []
    for i in range(50):
        points.append(0)

    state_obj = StateData
    count = 0
    for count, i in enumerate(state_obj.states):
        if snow == "19":
            if state_obj.states[count]["snow"] >= 19:
                points[count] += 1
        elif snow == "18":
            if state_obj.states[count]["snow"] <= 18:
                points[count] += 1
        if rural == "rural":
            if state_obj.states[count]["rural_urban"] == "rural":
                points[count] += 1
        elif rural == "urban":
            if state_obj.states[count]["rural_urban"] == "urban":
                points[count] += 1
        if tax == "yes":
            if state_obj.states[count]["income_tax"] == "yes":
                points[count] += 1
        elif tax == "no":
            if state_obj.states[count]["income_tax"] == "no":
                points[count] += 1
        if rain == "42":
            if state_obj.states[count]["rain"] >= 42:
                points[count] += 1
        elif rain == "41":
            if state_obj.states[count]["rain"] <= 41:
                points[count] += 1
        if coast == "yes":
            if state_obj.states[count]["coastline"] == "yes":
                points[count] += 1
        elif coast == "no":
            if state_obj.states[count]["coastline"] == "no":
                points[count] += 1
        if income == "high":
            if state_obj.states[count]["avg_income"] >= 70000:
                points[count] += 1
        elif income == "low":
            if state_obj.states[count]["avg_income"] <= 69999:
                points[count] += 1
        if political == "liberal":
            if state_obj.states[count]["political_climate"] == "liberal":
                points[count] += 1
        elif political == "conservative":
            if state_obj.states[count]["political_climate"] == "conservative":
                points[count] += 1
        if university == "yes":
            if state_obj.states[count]["university"] != "none":
                points[count] += 1
        elif university == "no":
            if state_obj.states[count]["university"] == "none":
                points[count] += 1
        if mountain == "yes":
            if state_obj.states[count]["mountains"] == "yes":
                points[count] += 1
        elif mountain == "no":
            if state_obj.states[count]["mountains"] == "no":
                points[count] += 1
        if desert == "yes":
            if state_obj.states[count]["desert"] == "yes":
                points[count] += 1
        elif desert == "no":
            if state_obj.states[count]["desert"] == "no":
                points[count] += 1
        if population == "high":
            if state_obj.states[count]["population"] >= 5895000:
                points[count] += 1
        elif population == "low":
            if state_obj.states[count]["population"] <= 5894999:
                points[count] += 1
        if waterfront == "yes":
            if state_obj.states[count]["waterfront"] == "yes":
                points[count] += 1
        elif waterfront == "no":
            if state_obj.states[count]["waterfront"] == "no":
                points[count] += 1
        if home == "high":
            if state_obj.states[count]["home_price"] >= 210000:
                points[count] += 1
        elif home == "low":
            if state_obj.states[count]["home_price"] <= 209999:
                points[count] += 1
        if crime == "yes":
            if state_obj.states[count]["crime_rate"] <= 20:
                points[count] += 1
        elif crime == "no":
            if state_obj.states[count]["crime_rate"] >= 21:
                points[count] += 1

    top_states = []
    max_points = max(points)
    for i, val in enumerate(points):
        if val == max_points:
            top_states.append(state_obj.states[i]["name"])
            max_points -= 1

    if not top_states:
        return flask.redirect(flask.url_for("sorry"))
    elif len(top_states) < 3:
        top_three_states = []
        for i in range(3):
            rando = random.choice(state_obj.states[i]["name"])
            top_three_states.append(rando)

        return flask.render_template(
            "suggest_page.html", point=points, final=top_three_states
        )
    elif top_states:
        top_three_states = []
        for i in top_states:
            rando = random.choice(top_states)
            top_states.remove(rando)
            top_three_states.append(rando)

        return flask.render_template(
            "suggest_page.html", point=points, final=top_three_states
        )

    return flask.render_template("sorry.html")


@app.route("/sorry", methods=["POST", "GET"])
def sorry():
    return flask.render_template("sorry.html")


@app.route("/dashboard", methods=["POST", "GET"])
def dashboard():
    """
    this is the dashboard page that will require the users to be logged in, this will lead users
    """

    return flask.render_template("dashboard.html")


@app.route("/about", methods=["POST", "GET"])
def about():
    """
    this is the page that has all the about us information
    """

    return flask.render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
