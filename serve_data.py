from flask import Flask, jsonify, Response, s
from os.path import join, dirname
import json
#from fetch_from_db import get_popular_artists

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')