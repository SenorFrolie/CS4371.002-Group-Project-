'''
this is the server file that defines all our routes and how our website is going to work
'''
import flask
from flask import request

app = flask.Flask(__name__)

@app.route('/')
def front_page():
    '''
    this is the very first page that the user will see when the visit our site
    '''
    return flask.render_template('front_page.html')

@app.route('/suggest_form', methods=['POST', 'GET'])
def suggest_form():
    '''
    this is the page where we will ask users their suggestions and retrieve their answers
    '''
    return flask.render_template('suggest_form.html')

@app.route('/suggest_page', methods=['POST', 'GET'])
def suggest_page():
    '''
    this is the page that will show the users suggestions and prompt them if they want to do it again
    '''
    snow_answer = request.form.get('snow_answer')
    drop_down_form = flask.request.form
    snow_answer = drop_down_form['snow_answer']
    rain_answer = drop_down_form['rain_answer']
    if snow_answer == 'yes' and rain_answer == 'no':
        return flask.render_template('suggest_page.html')

if __name__ == '__main__':
    app.run(debug=True)
