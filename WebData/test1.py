import imdb_license
import json
import requests

url = "https://imdb8.p.rapidapi.com/auto-complete"

querystring = {"q":"Peter Dinklage"}

headers = {
    'x-rapidapi-key': imdb_license.imdb_key,
    'x-rapidapi-host': imdb_license.imdb_host
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
data = json.loads(response.text)
print(json.dumps(data, indent=2))

print(type(data))
