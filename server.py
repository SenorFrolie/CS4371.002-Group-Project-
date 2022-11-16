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
    rural = drop_down_form["snow_answer"]
    tax = drop_down_form["snow_answer"]
    rain = drop_down_form["snow_answer"]
    coast = drop_down_form["snow_answer"]
    income = drop_down_form["snow_answer"]
    political = drop_down_form["snow_answer"]
    university = drop_down_form["snow_answer"]
    mountains = drop_down_form["snow_answer"]
    desert = drop_down_form["snow_answer"]
    population = drop_down_form["snow_answer"]
    waterfront = drop_down_form["snow_answer"]
    home = drop_down_form["snow_answer"]
    crime = drop_down_form["snow_answer"]

    #         'snow': 2,
    #         'rural_urban': 'rural',
    #         'income_tax': 'yes',
    #         'rain': 56,
    #         'coastline': 'yes',
    #         'avg_income': 51700,
    #         'political_climate': 'conservative',
    #         'university': 'none',
    #         'mountains': 'no',
    #         'desert': 'no',
    #         'population': 5039877,
    #         'waterfront': 'yes',
    #         'home_price': 138000,
    #         'crime_rate': 37
    

    return flask.render_template("suggest_page.html")


@app.route("/dashboard", methods=["POST", "GET"])
def dashboard():
    """
    this is the dashboard page that will require the users to be logged in, this will lead users
    """

    return flask.render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)
