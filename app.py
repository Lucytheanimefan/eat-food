import os
import requests
import json
from requests.auth import HTTPBasicAuth
from flask import Flask, request, jsonify
from flask import render_template
from nutritionix import Nutritionix
import requests
import json
import nutrientCalculator
from nutrientCalculator import get_info

app = Flask(__name__)



nix = Nutritionix(app_id='7f770e5d', api_key='dae4065c600b6b161789a27471167ccd') #make these env variables later
url = 'https://api.nutritionix.com/v1_1/search?'



@app.route("/results")
def results():
	#print nix.search('pizza').json()
	return render_template('results.html')

@app.route("/home")
@app.route("/")


def hello():
  
  return render_template('main.html')


# restriction shoul be the array of String in "allergen_contains_eggs" format
# calories_max is from the profile 
# limit number should be 10 for getting 10 meal suggestion
# if getting 10 more, have offset_value = 10, otherwise 0 
def getMeanlPlan(restrictions, calories_max, limit_number, offset_value):
 response = nix.search().nxql(
  filters={
  "nf_calories": {
  "lte": calories_max
  }
  #,
  #for res in restrictions:
  #  res : "None"
  },
  offset = offset_value,
  limit = limit_number,
  fields=["item_name", "item_id", "nf_calories", "allergen_contains_fish"]
  ).json()
 print response

'''

{u'allergen_contains_eggs': None,
 u'allergen_contains_fish': None,
 u'allergen_contains_gluten': None,
 u'allergen_contains_milk': None,
 u'allergen_contains_peanuts': None,
 u'allergen_contains_shellfish': None,
 u'allergen_contains_soybeans': None,
 u'allergen_contains_tree_nuts': None,
 u'allergen_contains_wheat': None,


  item = [{
  'appId':'7f770e5d',
  'appKey':'dae4065c600b6b161789a27471167ccd',
  'filters':{'nf_calories':{
  'from':50,
  'to':500
  },
  'nf_sodium':{
  'lte':200
  }
  },
  'limit':2,
  }]

  data = json.dumps(item)
  #print data
  response = requests.get(url, data=data)
  if response.status_code == 401:
    response = requests.get(url, auth=HTTPBasicAuth('spothorse9.lucy@gmail.com', 'hackduke7'))
    print response

'''



if __name__ == '__main__':
    a = ['allergen_contains_fish', 'allergen_contains_gluten'] 
    getMeanlPlan(a, 50, 5, 0)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


#get_info(gender_string, age_string, height_feet, height_inches, weight_string, activity_level)
@app.route("/getResults",methods=['POST','GET'])
def getResults():
	print "---------------------in getResults"
	print request.json
	json = get_info(request.json['gender'], request.json['age'],request.json['height_ft'],request.json["height_in"],request.json['weight'],request.json['activity'])
	return jsonify(result=json)

