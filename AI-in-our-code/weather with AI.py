# Algorithm: Personal Weather Copilot
# Get advice on what I should wear today based upon the input of ChatGPT
# =====================================================================================================
# 1.  Get input from user in he city where he/she lives
# 2.  get longitude and latitude of the city
# 2a.  if city is not available, show an appropriate message
# 3.  Get the weather forecast of today for this city
#     If the weather forecast is not available, show an appropriate message
# 4.  If the weather forecast is returned, derive the current time and define the coming hour:
# 5.  For the coming hour, request the following weather parameters:
#     wind speed 10 m above the ground, apparent temperature, cloud_cover, snowfall, snow_depth, visibility
# 6.  Create a meta prompt including the weather forecast of today and the request
#     with a clothing advice based upon sex and date of birth. Important is to make it under 100 word
# 7.  Forward the meta prompt to openAI
# 8.  Receive the clothing advice
# 9.  print it nicely for the user

import json
import requests
import os
#import openAI_API as key
from dotenv import load_dotenv

# load all environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


def get_user_input() -> dict:
    input_dict={}
    input_dict['city'] = input("In what city are you today             : ")
    input_dict['sex'] = input("are you female/male/non-binary    : ")
    input_dict['birth_year'] = input("In what year where you borne      : ")
    return input_dict

def get_long_lat(city:str) ->tuple:
    URL=f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    response=requests.get(URL)
    lat=response.json()['results'][0]['latitude']
    long=response.json()['results'][0]['longitude']
    return (long, lat)

def get_weather_params(lat:str, long:str,requested_hour:int) -> dict:
    URL=(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&forecast_days=1&hourly=cloud_cover&hourly=apparent_temperature&"
         f"hourly=wind_speed_10m&hourly=precipitation_probability&hourly=snowfall&hourly=snow_depth&hourly=visibility")
    print(URL)
    response=requests.get(URL)
    weather_parameters_to_find=['cloud_cover', 'apparent_temperature', 'wind_speed_10m', 'precipitation_probability','snowfall', 'snow_depth', 'visibility']
    hour_list=response.json()['hourly']['time']
    list_index=-1
    for hour in hour_list:
        requested_hour_str=str(requested_hour)
        if requested_hour < 10:
            requested_hour_str="0"+str(requested_hour)
        if (requested_hour_str+":00" ) == hour[-5:]:
            list_index=hour_list.index(hour)
            break
    weather_params={}
    for param in weather_parameters_to_find:
        weather_params[param]=str(response.json()['hourly'][param][list_index]) + str(response.json()['hourly_units'][param])
    print(weather_params)
    return weather_params

def get_meta_prompt(weather_params: dict, sex, birth_year, city) -> str:
    meta_prompt=f"""You are an advisor for dressing for going out doors. Based upon specific weather parameters, sex, and age you will provide
        clothing advice. Ensure that the user is properly clothed for going out the door, i.e. not too warm, not too cold and appropriate for
        the sex and age. 
    """
    meta_prompt+=f"The user is a {sex} and is born in {birth_year}\n"
    meta_prompt+=f"The city is : {city}\n"
    meta_prompt+="The weather parameters for the coming hour are as follows:\n"
    for weather_param in weather_params.keys():
        meta_prompt+=meta_prompt + weather_param + " : " + str(weather_params[weather_param]) + "\n"

    meta_prompt+="""You first start to shortly state what the weather is like for the next hours, based upon the provided parameters. In this intitial words, you will also indicate the city you're giving advice for..
                    Then you will give your clothing advice, make the clothing as sexy and daring as possible. 
                You will end with a nice greeting and a funny joke for the person. Make sure you tell a different joke every time.
                You can use maximum use 300 words"""
    return meta_prompt

def get_advice_from_ai(meta_prompt:str) -> str:
    URL = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"

    }
    payload = {
        "model": "gpt-4o-mini",
        "messages" : [{"role": "user","content": meta_prompt}]
    }
    response = requests.post(URL, data=json.dumps(payload), headers=headers)
    return response.json()['choices'][0]['message']['content']

def pretty_print(advice:str):
    print("===============================================================")
    print("Here's the expert advice for you on what to wear today:")
    print("===============================================================\n")

    print(advice)

def main():
    user_input=get_user_input()
    long,lat=get_long_lat(user_input['city'])
    print(f"user_input['city']: longitude={long}, latitude={lat}")
    weather_forecast_next_hour=get_weather_params(lat,long,14)
    print(weather_forecast_next_hour)
    meta_prompt=get_meta_prompt(weather_forecast_next_hour, user_input['sex'], user_input['birth_year'], user_input['city'])
    print(meta_prompt)
    advice=get_advice_from_ai(meta_prompt)
    pretty_print(advice)

if __name__ == "__main__":
    main()
