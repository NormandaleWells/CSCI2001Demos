import imdb_license
import json
import requests
import sys


# find all matches to the given name
def get_auto_complete(name):

    url = "https://imdb8.p.rapidapi.com/auto-complete"
    querystring = {"q":name}
    headers = {
        'x-rapidapi-key': imdb_license.imdb_key,
        'x-rapidapi-host': imdb_license.imdb_host
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    # print(json.dumps(data, indent=2))
    return data


def find_id(name, match_list):

    if len(match_list) == 0:
        print("Sorry, no matches for", name)
        sys.exit()

    elif len(match_list) == 1:
        match_id = match_list[0]['id']
        match_name = match_list[0]['l']
        print("Found {}, id = {}, name = {}".format(name, match_id, match_name))

    else:
        for i in range(len(match_list)):
            match = match_list[i]
            match_id = match["id"]
            match_name = match["l"]
            if match_id[:2] == 'nm':
                print("{} : {} (id = {})".format(i, match_id, match_name))
        choice = int(input("Which do you want? "))
        match_id = match_list[choice]['id']

    return match_id


def get_filmography(person_id):
    url = "https://imdb8.p.rapidapi.com/actors/get-all-filmography"
    querystring = {"nconst" : person_id}
    headers = {
        'x-rapidapi-key': imdb_license.imdb_key,
        'x-rapidapi-host': imdb_license.imdb_host
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    #print(json.dumps(data, indent=2))
    return data

    
if __name__ == "__main__":

    name = input("Enter a name: ")
    search_results = get_auto_complete(name)
    person_id = find_id(name, search_results['d'])

    filmography = get_filmography(person_id)
    film_list = filmography['filmography']
    for film in film_list:
        title_type = film['titleType']
        title = film['title']
        film_id = film['id']
        if title_type == "movie":
            print("{} : {} ({})".format(film_id, title, title_type))
