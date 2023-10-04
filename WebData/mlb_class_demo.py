import requests
import json


def get_player_data(name):
    url = "https://lookup-service-prod.mlb.com/json/named.search_player_all.bam"
    params = { "active_sw" : "'N'", "name_part" : "'"+name+"'" }
    response = requests.request("GET", url, headers={}, params=params)
    player_list = json.loads(response.text)
    # print(json.dumps(player_list, indent=2))
    return player_list


def get_player_teams(player_id):
    url = "https://lookup-service-prod.mlb.com/json/named.player_teams.bam"
    params = { "player_id" : "'"+str(player_id)+"'" }
    response = requests.request("GET", url, headers={}, params=params)
    player_teams = json.loads(response.text)
    # print(json.dumps(player_teams, indent=2))
    return player_teams


def print_one_team(team):
    name = team["team_brief"]
    end_date = team["end_date"]
    start_date = team["start_date"]
    print("\t", name, "from", start_date[:10], "to", end_date[:10])

    
def print_player_data(player_data):
    player_id = player_data["player_id"]
    name = player_data["name_display_first_last"]
    pro_debut_date = player_data["pro_debut_date"]
    print(name, " has player ID =", player_id, "and debuted on", pro_debut_date)

    player_teams = get_player_teams(player_id)
    query_results = player_teams["player_teams"]["queryResults"]
    if int(query_results["totalSize"]) == 1:
        print_one_team(query_results["row"])
    else:
        for team_data in query_results["row"]:
            print_one_team(team_data)


if __name__ == "__main__":

    player_list = get_player_data("Banks%")
    query_results = player_list["search_player_all"]["queryResults"]

    # This API is a bit odd.  If we get a single result, then
    # query_results["row"] is a dictionary containing data for
    # that one player.  Otherwise, we get a list of dictionaries.
    if int(query_results["totalSize"]) == 1:
        player_data = player_list["search_player_all"]["queryResults"]["row"]
        # print(json.dumps(player_data, indent=2))
        print_player_data(player_data)
    else:
        for player_data in query_results["row"]:
            print_player_data(player_data)
