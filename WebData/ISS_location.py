import json
import requests
import time

# see https://wheretheiss.at/w/developer

def get_satellite_list():
    url = "https://api.wheretheiss.at/v1/satellites"
    querystring = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, params=querystring)
    print("Satellite list (json):", response.text)
    return json.loads(response.text)


def get_satellite_data(sat_id):
    url = f"https://api.wheretheiss.at/v1/satellites/{sat_id}"
    querystring = {"units" : "miles"}
    headers = {}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return json.loads(response.text)


def get_location_data(lat, lng):
    url = f"https://api.wheretheiss.at/v1/coordinates/{lat},{lng}"
    querystring = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return json.loads(response.text)

    
if __name__ == "__main__":

    sat_list = get_satellite_list()
    print(sat_list)
    id = None
    for sat in sat_list:
        print(f'{sat["id"]} : {sat["name"]}')
        if sat["name"] == "iss":
            id = sat["id"]

    if id == None:
        print("No record for the iss!")
    else:
        while True:
    
            sat_data = get_satellite_data(id)
            lat = sat_data["latitude"]
            lng = sat_data["longitude"]
            alt = sat_data["altitude"]
            vel = sat_data["velocity"]
            print(f"lat: {lat}\nlng: {lng}\nalt: {alt}\nvel: {vel}\n")

            loc_data = get_location_data(lat, lng)
            tz = loc_data["timezone_id"]
            country = loc_data["country_code"]
            map_url = loc_data["map_url"]
            print(f"{country} {tz} {map_url}\n")
            time.sleep(10)
