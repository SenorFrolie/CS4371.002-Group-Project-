import flask

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

if __name__ == '__main__':
    app.run(debug=True)