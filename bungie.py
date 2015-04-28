import json

import requests

ACTIVITY_URL = 'http://www.bungie.net/Platform/Destiny/Advisors/?definitions=True'

def fetch_activities():
    http_response = requests.get(ACTIVITY_URL)
    json_response = http_response.json()
    api_response = json_response['Response']
    return api_response

def process_activities(api_response):
    """
    Processes a Bungie API response by pulling out activity data from the rest
    of the information. These definitions will be further processed into
    less obscured dictionaries by other functions.
    """

    activity_map = {}

    nightfall_hash = str(api_response['data']['nightfallActivityHash'])
    daily_hashes = api_response['data']['dailyChapterHashes']
    heroic_hashes = api_response['data']['heroicStrikeHashes']
    crucible_hash = str(api_response['data']['dailyCrucibleHash'])

    activities = api_response['definitions']['activities']

    activity_map['nightfall'] = activities[nightfall_hash]

    activity_map['crucible'] = activities[crucible_hash]

    dailies_info = []
    for d_hash in daily_hashes:
        dailies_info.append(activities[str(d_hash)])

    activity_map['daily'] = dailies_info

    heroics_info = []
    for h_hash in heroic_hashes:
        heroics_info.append(activities[str(h_hash)])

    activity_map['heroic'] = heroics_info

    return activity_map

def process_nightfall(activity_map):
    nightfall_info = activity_map['nightfall']
    description = nightfall_info['activityDescription']
    skulls = nightfall_info['skulls']
    mods = [s['displayName'] for s in skulls]

    title = nightfall_info['activityName']

def process_crucible(activity_map):
    # Note: 'skulls' is an empty list in Crucible
    pass


if __name__ == '__main__':
    act_json = fetch_activities()
    activities = process_activities(act_json)
