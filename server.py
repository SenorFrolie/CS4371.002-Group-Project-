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

    snow_answer = request.form.get("snow_answer")
    drop_down_form = flask.request.form
    snow_answer = drop_down_form["snow_answer"]
    rain_answer = drop_down_form["rain_answer"]
    for i in range(50):
        if snow_answer == drop_down_form["snow answer"]:
            print("hoopla")

    if snow_answer == "yes" and rain_answer == "no":
        return flask.render_template("suggest_page.html")


@app.route("/dashboard", methods=["POST", "GET"])
def dashboard():
    """
    this is the dashboard page that will require the users to be logged in, this will lead users
    """

    return flask.render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)
