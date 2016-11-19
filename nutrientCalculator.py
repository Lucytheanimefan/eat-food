def convert_height(feet, inches):
    """
    Converts height given in feet and inches into height in centimeters
    :param feet: number of feet
    :param inches: number of inches
    :return: height in centimeters
    """
    total_inches = feet*12 + inches
    centimeters = total_inches*2.54
    return centimeters

def convert_weight(pounds):
    """
    Converts weight given in pounds into weight in kilograms
    :param pounds: number of pounds
    :return: weight in kilograms
    """
    kilograms = pounds*0.453592
    return kilograms

def get_activity_factor(activity):
    """
    Converts activity level into an activity factor
    :param activity: string describing activity level
    :return: activity factor
    """
    activity_level_map = {"bmr": 1, "sedentary": 1.2, "mild": 1.375, "moderate": 1.55, "heavy": 1.7, "extreme": 1.9}
    activity_factor = activity_level_map[activity]
    return activity_factor

def calculate_calories(gender, age, height, weight, activity_factor):
    """
    Calculates the number of calories an individual should consume in a day
    :param gender: gender of individual
    :param age: age of individual
    :param height: height of individual in centimeters
    :param weight: weight of individual in kilograms
    :param activity_factor: the factor by which the BMR is multiplied
    :return: the number of calories to consume
    """
    BMR = 0
    #Mifflin - St Jeor equation
    if (gender == "male"):
        BMR = 10*weight + 6.25*height - 5*age + 5
    else:
        BMR = 10 * weight + 6.25 * height - 5 * age - 161
    return BMR*activity_factor

def calculate_daily_values(calories):
    """
    Calculates the recommended daily values for each nutrient based on the number of calories to consume
    :param calories: number of calories the individual should consume
    :return: dictionary containing the recommended daily values where the key is the nutrient
    """
    daily_value_2000 = {"total_fat": 65, "saturated_fat": 20, "trans_fat": 0, "cholesterol": 0.3, "sodium": 2.4,
                       "carbohydrate": 300, "dietary_fiber": 25, "protein": 50, "sugar": 25, "vitaminA": 0.0015,
                       "vitaminC": 0.06}
    daily_values = {}
    for nutrient in daily_value_2000:
        daily_values[nutrient] = daily_value_2000[nutrient]*calories/2000
    return daily_values

def get_info(gender_string, age_string, height_feet, height_inches, weight_string, activity_level):
    gender = gender_string.lower()
    age = age_string
    height = convert_height(height_feet, height_inches)
    weight = convert_weight(weight_string)
    activity_level = (activity_level.split(' ')[0]).lower()
    activity_factor = get_activity_factor(activity_level)
    calories = calculate_calories(gender, age, height, weight, activity_factor)

    info = calculate_daily_values(calories)
    info["calories"] = calories
    return info