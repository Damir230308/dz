from flask import Flask, Response
from flask import request

app = Flask(__name__)

@app.route('/<string:search>')
def index(search: str):
    name = request.args.get('search', None)
    return f'Hello {search}'
