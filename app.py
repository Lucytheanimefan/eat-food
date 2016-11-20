import os
from flask import Flask, request, jsonify
from flask import render_template
from nutritionix import Nutritionix
import requests
import json
import nutrientCalculator
from nutrientCalculator import get_info
from mealPlan import getMealPlan

app = Flask(__name__)

nix = Nutritionix(app_id="7f770e5d", api_key="dae4065c600b6b161789a27471167ccd") #make these env variables later

@app.route("/results")
def results():
	return render_template('results.html')

@app.route("/login")
def login():
	return render_template('login.html')

@app.route("/home")
@app.route("/")
def hello():
	return render_template('main.html')

#get_info(gender_string, age_string, height_feet, height_inches, weight_string, activity_level)
@app.route("/getResults",methods=['POST','GET'])
def getResults():
	print "---------------------in getResults"
	print request.json
	info = get_info(request.json['gender'], request.json['age'],request.json['height_ft'],request.json["height_in"],request.json['weight'],request.json['activity'])
	return jsonify(result=json)

if __name__ == "__main__":
	print getMealPlan(["eggs","fish","gluten"],100, 5, 5, "vegetable")
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)