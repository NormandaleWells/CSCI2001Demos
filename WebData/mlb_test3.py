import http.client
import json
import requests

# see https://appac.github.io/mlb-data-api-docs/#player-data-player-search-get

conn = http.client.HTTPSConnection("lookup-service-prod.mlb.com")

headers = {}

# when using http.client, replace "special" characters with their
# %xx hex representation.
#       space = %20
#       %     = %25
# apparently, % represents a wild-card character for searches
conn.request("GET", "/json/named.search_player_all.bam?name_part='Ernie%20Banks'&sport_code='mlb'&active_sw='N'", headers=headers)

res = conn.getresponse()
data = res.read()

print("http.client")
print(json.dumps(json.loads(data), indent=2))




# see https://appac.github.io/mlb-data-api-docs/#player-data-player-search-get

url = "https://lookup-service-prod.mlb.com/json/named.search_player_all.bam"

# when using the requests module, just use special characters,
# not the %xx representation
querystring = {"name_part":"'Banks%'","sport_code":"'mlb'","active_sw":"'N'"}

headers = {}

response = requests.request("GET", url, headers=headers, params=querystring)
data = json.loads(response.text)

print("requests")
print(json.dumps(data, indent=2))
