from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

from RouteSelector.handler import *
from RouteSelector.models import *

@app.route('/', methods=['GET'])
def index():
    return "<div>Server is Online</div>"

@app.route('/api', methods=['GET'])
def api():
    data = '''
    <h1>Route Selector API</h1>
    <p>Welcome to Python Route Selector API</p>
    <p>©Muhammad Talal Majeed</p>
    '''
    return data

app.run(debug=True, host='0.0.0.0', port=2342)