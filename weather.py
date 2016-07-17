#Weather API call - prints current weather to command line

import json, sys, requests

if len(sys.argv) < 2:
	print("Usage: weather.py location")
	sys.exit()
location = " ".join(sys.argv[1:])

url = "http://api.openweathermap.org/data/2.5/forecast/daily?q={}&cnt=3&APPID=XXXXXXXXX".format(location)
response = requests.get(url)
response.raise_for_status()

weather_data = json.loads(response.text)
w = weather_data['list']

print("Current weather in %s:" % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print("\nTomorrow:")
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
