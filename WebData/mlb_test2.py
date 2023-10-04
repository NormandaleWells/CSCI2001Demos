import json
import mlb_license
import requests

url = "https://mlb-data.p.rapidapi.com/json/named.search_player_all.bam"

querystring = {"name_part":"'Ernie Banks'","sport_code":"'mlb'","active_sw":"'N'"}

headers = {
    'x-rapidapi-key': mlb_license.mlb_key,
    'x-rapidapi-host': mlb_license.mlb_host
    }

response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.text)
print(json.dumps(data, indent=2))
