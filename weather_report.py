import json
import urllib.request
import urllib.parse

baseurl = 'https://api.openweathermap.org/data/2.5/weather?q='
api_key = 'API_KEY'    #Create an account in https://home.openweathermap.org/users/sign_in and paste your personal API_KEY here
location = input("Enter location: ")
complete_url = baseurl + location + '&APPID=' + api_key + '&units=metric'
info = json.loads(urllib.request.urlopen(complete_url).read().decode('utf-8'))

print("Weather status in", info["name"])
print("Weather: ", info["weather"][0]["main"])
print("Weather description: ", info["weather"][0]["description"].capitalize())
print("Temperature: ", str(info["main"]["temp"]) + "°C")
print("Feels: ", str(info["main"]["feels_like"]) + "°C")
print("Wind speed: ", str(info["wind"]["speed"]) + "m/s")
