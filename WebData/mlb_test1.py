import json
import mlb_license
import requests

url = "https://mlb-data.p.rapidapi.com/json/named.player_teams.bam"

querystring = {"player_id" : "'493316'", "season" : "'2014'"}

headers = {
    'x-rapidapi-key': mlb_license.mlb_key,
    'x-rapidapi-host': mlb_license.mlb_host
    }

response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.text)
print(json.dumps(data, indent=2))
