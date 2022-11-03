import flask

app = flask.Flask(__name__)
@app.route('/')
def front_page():
    return flask.render_template('front_page.html')

if __name__ == '__main__':
    app.run(debug=True)