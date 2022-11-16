"""
this is the server file that defines all our routes and how our website is going to work
"""
import flask
from flask import request

from city_data import CityInfo
from state_data import StateData

app = flask.Flask(__name__)


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
    tax = drop_down_form["tax_answer"]
    political = drop_down_form["political_answer"]
    university = drop_down_form["uni_answer"]
    mountain = drop_down_form["mountain_answer"]
    desert = drop_down_form["desert_answer"]
    population = drop_down_form["pop_answer"]
    waterfront = drop_down_form["water_answer"]
    home = drop_down_form["home_answer"]
    crime = drop_down_form["crime_answer"]

    points = []
    for i in range(50):
        points[i] = 0

    state_obj = StateData
    count = 0
    for i in state_obj.states:
        if snow == 'yes':
            if state_obj.states[count]['snow_anser'] == 'yes':
                points[count] += 1
        elif snow == 'no':
            if state_obj.states[count]['snow_anser'] == 'no':
                points[count] += 1
        if rural == 'yes':
            if state_obj.states[count]['rural_anser'] == 'yes':
                points[count] += 1
        elif rural == 'no':
            if state_obj.states[count]['rural_anser'] == 'no':
                points[count] += 1
    
    print(points)

    return flask.render_template("suggest_page.html")


@app.route("/dashboard", methods=["POST", "GET"])
def dashboard():
    """
    this is the dashboard page that will require the users to be logged in, this will lead users
    """

    return flask.render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)
