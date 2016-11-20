from nutritionix import Nutritionix


nix = Nutritionix(app_id="7f770e5d", api_key="dae4065c600b6b161789a27471167ccd") #make these env variables later

# restriction should be the array of food restrictions, each element would be the string name
# calories_max is from the profile 
# limit number should be 10 for getting 10 meal suggestion
# if getting 10 more, have offset_value = 10, otherwise 0 
def getMealPlan(restrictions, calories_max, limit_number, offset_value, food_type):
  fields = ["allergen_contains_"+food for food in restrictions]
  fields = fields + ["item_name", "item_id", "nf_calories","nf_ingredient_statement"]
  response = nix.search().nxql(
    filters={
    "nf_calories": {
    "lte": calories_max,
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

  return response

#value = response["food"]