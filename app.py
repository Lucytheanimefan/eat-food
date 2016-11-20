import os
import json
import requests
import server
from requests.auth import HTTPBasicAuth
from flask import Flask, request, jsonify,redirect, url_for
from flask import render_template
from nutritionix import Nutritionix
from nutrientCalculator import write_info
from mealPlan import getMealPlan
from login import *

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


@app.route("/login",methods=['POST','GET'])
def login():
	open_account(request.json['username'], request.json['password'])
	set_username(request.json['username'])
	redirect(url_for('search'))


@app.route("/createaccount",methods=['POST','GET'])
def createaccount():
	return create_account(request.json['username'], request.json['password'])

@app.route("/")
def hello():
	return render_template('login.html')

@app.route("/search")
def search():
	return render_template('main.html')

@app.route("/journal")
def journal():
	return render_template('journal.html')

#get_info(gender_string, age_string, height_feet, height_inches, weight_string, activity_level)
@app.route("/getResults",methods=['POST','GET'])
def getResults():
	print "---------------------in getResults"
	print request.json
	info = write_info(username, request.json['gender'], request.json['age'],request.json['height_ft'],request.json["height_in"],request.json['weight'],request.json['activity'], request.json['restrictions'])
	return jsonify(result=json)

if __name__ == "__main__":
	document = db.users.find({"username": "amanocha"})[0]
	restrictions = document["restrictions"]
	calories_min = document["calories"]
	max_total_fat = document["total_fat"]
	max_cholesterol = document["cholesterol"]
	max_saturated_fat = document["saturated_fat"]
	max_sodium = document["sodium"]
	max_sugar = document["sugar"]
	getMealPlan(restrictions,calories_min, 50, 5, "vegetable",max_total_fat,
	max_cholesterol, max_saturated_fat,max_sodium, max_sugar)

	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
