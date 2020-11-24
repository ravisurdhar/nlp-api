from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return {
    'status': 'success',
    'code': 200,
    'data': {
    	'text': 'App Works!'
    	}
    }

@app.route('/tag/<text>')
def tagger(text):
    return {
    'status': 'success',
    'code': 200,
    'data': {
    	'text': text
    	}
    }

@app.errorhandler(404)
def page_not_found(error):
    return {
    'status': 'error',
    'code': 404,
    'message': {
    	'text': 'Page Not Found'
    	}
    }, 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)