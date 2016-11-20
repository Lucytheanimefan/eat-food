from nutritionix import Nutritionix


nix = Nutritionix(app_id="7f770e5d", api_key="dae4065c600b6b161789a27471167ccd") #make these env variables later

# restriction should be the array of food restrictions, each element would be the string name
# calories_max is from the profile 
# limit number should be 10 for getting 10 meal suggestion
# if getting 10 more, have offset_value = 10, otherwise 0 
def getMealPlan(restrictions, calories_min, limit_number, offset_value, food_type, 
  max_total_fat, max_cholesterol, max_saturated_fat, max_sodium, max_sugar):
  fields = ["allergen_contains_"+food for food in restrictions]
  fields = fields + ["item_name", "nf_calories",'nf_vitamin_a_dv', 'nf_vitamin_c_dv',
   'nf_total_fat', 'nf_total_carbohydrate', 'nf_saturated_fat', 'nf_sodium', 'nf_sugars', 'nf_cholesterol', 
   'nf_dietary_fiber','nf_protein','nf_calcium_dv', 'nf_iron_dv']
  response = nix.search().nxql(
    filters={
    "nf_calories": {
    "lte": calories_min * 1.5,
    "not":{
     "item_type":1, #not from restaurant
     "nf_serving_weight_grams":None
    }
    }
  },
  query = food_type,
  offset = offset_value,
  limit = limit_number,
  fields = fields
  ).json()

  allFood = []  

  for i in response['hits']:
    tel = {}  
    item_i = i['fields']
    tel['calories'] = item_i['nf_calories']
    tel['name'] = item_i['item_name']
    tel['vitamin_a'] = item_i['nf_vitamin_a_dv']
    tel['vitamin_c'] = item_i['nf_vitamin_c_dv']
    tel['total_fat'] = item_i['nf_total_fat']
    tel['carbs'] = item_i['nf_total_carbohydrate']
    tel['saturated_fat'] = item_i['nf_saturated_fat']
    tel['sodium'] = item_i['nf_sodium']
    tel['sugar'] = item_i['nf_sugars']
    tel['cholesterol'] = item_i['nf_cholesterol']
    tel['fiber'] = item_i['nf_dietary_fiber']
    tel['protein'] = item_i['nf_protein']
    tel['calcium'] = item_i['nf_calcium_dv']
    tel['iron'] = item_i['nf_iron_dv']
    allFood.append(tel)


  print allFood.pop()['name']
     

  return response

