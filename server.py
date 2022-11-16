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
    #for i in state_obj.states:
    for count, i in enumerate(state_obj.states):
        if snow == "yes":
            if state_obj.states[count]["snow"] == "yes":
                points[count] += 1
        elif snow == "no":
            if state_obj.states[count]["snow"] == "no":
                points[count] += 1
        if rural == "yes":
            if state_obj.states[count]["rural_urban"] == "yes":
                points[count] += 1
        elif rural == "no":
            if state_obj.states[count]["rural_urban"] == "no":
                points[count] += 1
        if tax == "yes":
            if state_obj.states[count]["income_tax"] == "yes":
                points[count] += 1
        elif tax == "no":
            if state_obj.states[count]["income_tax"] == "no":
                points[count] += 1
        if rain == "yes":
            if state_obj.states[count]["rain"] == "yes":
                points[count] += 1
        elif rain == "no":
            if state_obj.states[count]["rain"] == "no":
                points[count] += 1
        if coast == "yes":
            if state_obj.states[count]["coastline"] == "yes":
                points[count] += 1
        elif coast == "no":
            if state_obj.states[count]["coastline"] == "no":
                points[count] += 1
        if income == "yes":
            if state_obj.states[count]["avg_income"] == "yes":
                points[count] += 1
        elif income == "no":
            if state_obj.states[count]["avg_income"] == "no":
                points[count] += 1
        if political == "yes":
            if state_obj.states[count]["political_climate"] == "yes":
                points[count] += 1
        elif political == "no":
            if state_obj.states[count]["political_climate"] == "no":
                points[count] += 1
        if university == "yes":
            if state_obj.states[count]["university"] == "yes":
                points[count] += 1
        elif university == "no":
            if state_obj.states[count]["university"] == "no":
                points[count] += 1
        if mountain == "yes":
            if state_obj.states[count]["mountains"] == "yes":
                points[count] += 1
        elif mountain == "no":
            if state_obj.states[count]["mountians"] == "no":
                points[count] += 1
        if desert == "yes":
            if state_obj.states[count]["desert"] == "yes":
                points[count] += 1
        elif desert == "no":
            if state_obj.states[count]["desert"] == "no":
                points[count] += 1
        if population == "yes":
            if state_obj.states[count]["population"] == "yes":
                points[count] += 1
        elif population== "no":
            if state_obj.states[count]["population"] == "no":
                points[count] += 1
        if waterfront == "yes":
            if state_obj.states[count]["waterfront"] == "yes":
                points[count] += 1
        elif waterfront == "no":
            if state_obj.states[count]["waterfront"] == "no":
                points[count] += 1
        if home == "yes":
            if state_obj.states[count]["home_price"] == "yes":
                points[count] += 1
        elif home == "no":
            if state_obj.states[count]["home_price"] == "no":
                points[count] += 1
        if crime == "yes":
            if state_obj.states[count]["crime_rate"] == "yes":
                points[count] += 1
        elif crime == "no":
            if state_obj.states[count]["crime_rate"] == "no":
                points[count] += 1

    print(points)

    return flask.render_template("suggest_page.html", point = points)


@app.route("/dashboard", methods=["POST", "GET"])
def dashboard():
    """
    this is the dashboard page that will require the users to be logged in, this will lead users
    """

    return flask.render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)
