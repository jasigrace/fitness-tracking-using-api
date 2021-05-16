import requests
from datetime import datetime

APP_ID = "YOUR_ID"
API_KEY = "YOUR_KEY"
BEARER_AUTH = "YOUR_AUTH"

natural_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
shetty_endpoint = "https://api.sheety.co/bd0cb97da38cd60c795d26776e4a6d9f/workoutTracking/workouts"

headers_natural_exercise = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

headers_shetty = {
    "Authorization": BEARER_AUTH,
}

user_input = input("Tell me which exercises you did: ")

params_natural_exercise = {
 "query": user_input,
 "gender": "female",
 "weight_kg": 46,
 "height_cm": 154,
 "age": 20
}


response_natural_exercise = requests.post(url=natural_exercise_endpoint,
                                          headers=headers_natural_exercise,
                                          json=params_natural_exercise)

for i in range(len(response_natural_exercise.json()['exercises'])):
    workout_name = response_natural_exercise.json()['exercises'][i]['name'].title()
    workout_duration = response_natural_exercise.json()['exercises'][i]['duration_min']
    workout_calories = response_natural_exercise.json()['exercises'][i]['nf_calories']
    workout_date = str(datetime.now().strftime("%x"))
    workout_time = str(datetime.now().strftime("%X"))

    workout_params = {
        "workout": {
            "date": workout_date,
            "time": workout_time,
            "exercise": workout_name,
            "duration": workout_duration,
            "calories": workout_calories,
            "id": 3,
        }
    }

    response_shetty = requests.post(url=shetty_endpoint, json=workout_params, headers=headers_shetty)
    print(response_shetty.text)
