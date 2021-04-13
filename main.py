# Learning how to use Riot API
# https://developer.riotgames.com/
# by Ze Song 4/13/2021
# Using python pycharm IDE
import requests

# LOL Status - https://developer.riotgames.com/apis#lol-status-v4/GET_getPlatformData

API_URL = "https://na1.api.riotgames.com/lol/status/v4/platform-data?api_key=RGAPI-62e2c65a-7367-4107-979f-a3d28e2b91cb"
response = requests.get(API_URL)

# print("id:", (response.json()['id']))
# print("Name:", (response.json()['name']))
# print("locales:", (response.json()['locales']))
# print("Maintenances:", (response.json()['maintenances']))
# print("Incidents:", (response.json()['incidents']))

# summoner  -  https://developer.riotgames.com/apis#summoner-v4/GET_getBySummonerName

API_URL = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/yunah?api_key=RGAPI-62e2c65a-7367-4107" \
          "-979f-a3d28e2b91cb "
response = requests.get(API_URL)

# print("Account ID:", (response.json()['accountId']))
# print("Profile Icon ID:", (response.json()['profileIconId']))
# print("Last Login:", (response.json()['revisionDate']))
# print("Name:", (response.json()['name']))
# print("Summoner ID:", (response.json()['id']))
# print("Puuid:", (response.json()['puuid']))
# print("Summoner Level:", (response.json()['summonerLevel']))

# LOL Status - https://developer.riotgames.com/apis#league-v4

API_URL = "https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner" \
          "/pQtoAZs0EtoUk6pgTJS5wnyRh322eP7kV9DCc4cXzkC9K4o?api_key=RGAPI-62e2c65a-7367-4107-979f-a3d28e2b91cb "
response = requests.get(API_URL)

print("leagueId:", (response.json()[0]['leagueId']))
print("summonerName:", (response.json()[0]['summonerName']))
print("queueType:", (response.json()[0]['queueType']))
print("tier:", (response.json()[0]['tier']))
print("rank:", (response.json()[0]['rank']))
print("leaguePoints:", (response.json()[0]['leaguePoints']))
print("wins:", (response.json()[0]['wins']))
print("hotStreak:", (response.json()[0]['hotStreak']))
print("veteran:", (response.json()[0]['veteran']))
print("freshBlood:", (response.json()[0]['freshBlood']))
print("inactive:", (response.json()[0]['inactive']))


