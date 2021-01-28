import requests

url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"q":"hyderabad ,india","lat":"0","lon":"0","callback":"test","id":"2172797","lang":"null","units":"\"metric\" or \"imperial\"","mode":"xml, html"}

headers = {
    'x-rapidapi-key': "0267e9fba2msh9bb91d9e84501e9p1eb587jsnb2a86b6ae3c3",
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)