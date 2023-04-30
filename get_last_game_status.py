import requests
from api_key import apiKey



# Replace <region> and <summonerName> with the actual region and summoner name
region = 'euw1'


# Set up the headers to include your API key and authorization
headers = {
    'X-Riot-Token': apiKey,
}

def get_summoner_data(summoner_name):
    global region
    global headers
    url = f'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}'
    # Searching user id
    response = requests.get(url, headers=headers)
    data = response.json()
    return data



def get_last_game_id(summoner_puuid):
    global headers
    match_history_url = f'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{summoner_puuid}/ids?count=1'
    response = requests.get(match_history_url, headers=headers)
    history = response.json()
    return history[0]

def is_won(game_id, summoner_id):
    global headers
    game_info_url = f"https://europe.api.riotgames.com/lol/match/v5/matches/{game_id}"
    response = requests.get(game_info_url, headers=headers)
    game_data = response.json()
    for participant in game_data['info']['participants']:
        if participant["summonerId"] == summoner_id:
            return participant['win']
    #should never happen
    return False

def is_last_game_won(summoner_name):
    summoner_data = get_summoner_data(summoner_name)
    summoner_id = summoner_data['id']
    summoner_puuid = summoner_data['puuid']
    return is_won(get_last_game_id(summoner_puuid), summoner_id)

print(get_summoner_data("Caca Malveillant"))