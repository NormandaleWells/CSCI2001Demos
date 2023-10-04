import imdb_license
import json
import requests

# I could not find a way to get to the IMDB API directly,
# so this is all going through rapidapi.com.
# See https://rapidapi.com/apidojo/api/imdb8


def get_auto_complete(name):

    # find all the matches to this name
    url = "https://imdb8.p.rapidapi.com/auto-complete"
    querystring = {"q" : name}
    headers = {
        'x-rapidapi-key' : imdb_license.imdb_key,
        'x-rapidapi-host' : imdb_license.imdb_host
        }
    response = requests.request("GET", url, headers=headers, params=querystring)

    # get the data as a json object
    return json.loads(response.text)


def find_id(name, match_list):

    # We need at least one match.
    if len(match_list) == 0:
        print("Sorry, no matches for", name)
        sys.exit()

    # If we got exactly one match, use it
    elif len(match_list) == 1:
        id = match_list[0]['id']
        this_name = match_list[0]['l']
        print(f"Found {name}, ID={id}, name={this_name}")

    # Other, let the user choose
    else:
        print(name, "matched the following:")
        for i in range(len(match_list)):
            id = match_list[i]['id']
            name = match_list[i]['l']
            print(f"{i}: {name} (id = {id})")
        choice = int(input("Which do you want? "))
        id = match_list[choice]['id']
    return id


def get_filmography(id):

    url = "https://imdb8.p.rapidapi.com/actors/get-all-filmography"
    querystring = {"nconst" : id}
    headers = {
        'x-rapidapi-key' : imdb_license.imdb_key,
        'x-rapidapi-host' : imdb_license.imdb_host
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return json.loads(response.text)


def get_top_cast(id):

    url = "https://imdb8.p.rapidapi.com/title/get-top-cast"
    querystring = {"tconst" : id}
    headers = {
        'x-rapidapi-key': imdb_license.imdb_key,
        'x-rapidapi-host': imdb_license.imdb_host
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return json.loads(response.text)


if __name__ == "__main__":

    # Get the name or ID.  If a non-ID is provided,
    # find the best match to the name.
    name = input("Name or ID: ")
    if name[:2] == "nm" or name[:2] == "tt":

        # if we were given an ID, use it
        id = name

    else:

        data = get_auto_complete(name)
#        print(json.dumps(data, indent=1))
        match_list = data['d']
        id = find_id(name, match_list)

    if id[:2] == "nm":
        filmography = get_filmography(id)
        film_list = filmography["filmography"]
        for film in film_list:
            title_type = film['titleType']
            title = film['title']
            film_id = film['id']
            print(f"{film_id} : {title} ({title_type})")
    elif id[:2] == 'tt':
        top_cast = get_top_cast(id)
        print(len(top_cast), "total cast.  Top 10:")
        for i in range(min(10, len(top_cast))):
            name = top_cast[i][6:-1]
            data = get_auto_complete(name)
            print(data['d'][0]['l'])
    else:
        print("Unknown ID type: ", id)
