from flask import Flask, render_template, jsonify, send_from_directory, request
import json
import pandas as pd
import numpy as np
import os
from modelHelper import ModelHelper

#init app and class
app = Flask(__name__)
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# modelHelper = ModelHelper()

#endpoint
# Favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

# Route to render index.html template
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")

@app.route("/maps")
def maps():
    # return template and dat
    return render_template("maps.html")

@app.route("/filter")
def filter():
    # return template and dat
    return render_template("filter.html")
@app.route("/calculate")
def calculate():
    # return template and dat
    return render_template("calculate.html")

@app.route("/contour")
def contour():
    # return template and dat
    return render_template("contour.html")

@app.route("/Wells")
def wellsummary():
    # return template and dat
    return render_template("Wells.html")

@app.route("/about")
def about():
    # return template and dat
    return render_template("about.html")

# @app.route("/makePrediction", methods=["POST"])
# def makePredictions():
#     content = request.json["data"]

#     # parse
#     sex_flag = int(content["sex_flag"])
#     age = float(content["age"])
#     fare = float(content["fare"])
#     familySize = int(content["familySize"])
#     p_class = int(content["p_class"])
#     embarked = content["embarked"]

    # #dummy data
    # sex_flag = 1
    # age = 25
    # fare = 25
    # familySize = 2
    # p_class = 1
    # embarked = "C"

    # prediction = modelHelper.makePredictions(sex_flag, age, fare, familySize, p_class, embarked)
    # print(prediction)
    # return(jsonify({"ok": True, "prediction": str(prediction)}))

####################################
# ADD MORE ENDPOINTS

###########################################

#############################################################

# @app.after_request
# def add_header(r):
#     """
#     Add headers to both force latest IE rendering engine or Chrome Frame,
#     and also to cache the rendered page for 10 minutes.
#     """
#     r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
#     r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
#     r.headers["Pragma"] = "no-cache"
#     r.headers["Expires"] = "0"
#     return r

#main
if __name__ == "__main__":
    app.run(debug=True)