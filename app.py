import os
import json
import requests
import server
from requests.auth import HTTPBasicAuth
from flask import Flask, request, jsonify
from flask import render_template
from nutritionix import Nutritionix
from nutrientCalculator import write_info
from mealPlan import getMealPlan
from login import create_account

app = Flask(__name__)
username = ""
db =  server.get_db()

nix = Nutritionix(app_id='7f770e5d', api_key='dae4065c600b6b161789a27471167ccd') #make these env variables later
url = 'https://api.nutritionix.com/v1_1/search?'

def set_username(new_username):
	global username
	username = new_username

@app.route("/results")
def results():
	return render_template('results.html')

@app.route("/createaccount",methods=['POST','GET'])
def createaccount():
	return create_account(request.json['username'], request.json['password'])

@app.route("/")
def hello():
	return render_template('login.html')

@app.route("/search")
def search():
	return render_template('main.html')


#get_info(gender_string, age_string, height_feet, height_inches, weight_string, activity_level)
@app.route("/getResults",methods=['POST','GET'])
def getResults():
	print "---------------------in getResults"
	print request.json
	info = write_info(request.json['gender'], request.json['age'],request.json['height_ft'],request.json["height_in"],request.json['weight'],request.json['activity'])
	return jsonify(result=json)

if __name__ == "__main__":
	document = db.users.find({"username": "amanocha"})[0]
	restrictions = document["restrictions"]
	calories = document["calories"]
	print getMealPlan(restrictions, calories, 5, 5, "vegetable")
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
