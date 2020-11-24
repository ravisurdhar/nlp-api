"""
A simple Flask API
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """
    Index
    """
    data = {'text': 'App Works!'}
    return {
        'status': 'success',
        'code': 200,
        'data': data
    }


@app.route('/tag/<text>')
def tagger(text):
    """
    Tagger endpoint
    """
    data = {'text': text}
    return {
            'status': 'success',
            'code': 200,
            'data': data
    }


@app.errorhandler(404)
def page_not_found(error):  # pylint: disable=unused-argument
    """
    404 handler
    """
    message = {'text': 'Page Not Found'}
    return {
           'status': 'error',
           'code': 404,
           'message': message
    }, 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
