import json

import requests

from strike import get_short_name

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

    :param api_response: A dictionary of the original Bungie API response
    :return dictionary: Dictionary mapping the nightfal, heroic, daily, and
                        crucible event information to these names.
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

def stringify_mods(mod_list):
    return ", ".join(mod_list)

def process_nightfall(activity_map):
    """
    :param activity_map: A dictionary of processed event information
    :return dictionary: A dictionary of the Nightfall's information
    """
    nightfall_info = activity_map['nightfall']
    description = nightfall_info['activityDescription']
    skulls = nightfall_info['skulls']
    mods = [s['displayName'] for s in skulls]

    title = nightfall_info['activityName']

    name = get_short_name(description)

    nf_dict = {'title': title,
               'description': description,
               'mods': stringify_mods(mods),
               'name': name,
    }

    return nf_dict

def process_heroic(activity_map):
    """
    :param activity_map: A dictionary of processed event information
    :return dictionary: A dictionary of the Heroic's information
    """
    heroic_acts = activity_map['heroic']

    # Here, we'll just use the first instance's information
    # since the only variation should be the levels.
    heroic_info = heroic_acts[0]
    description = heroic_info['activityDescription']
    skulls = heroic_info['skulls']
    mods = [s['displayName'] for s in skulls]

    title = heroic_info['activityName']

    name = get_short_name(description)

    heroic_dict = {'title': title,
                   'description': description,
                   'mods': stringify_mods(mods),
                   'name': name,
    }
    return heroic_dict

def process_daily(activity_map):
    """
    :param activity_map: A dictionary of processed event information
    :return dictionary: A dictionary of the Daily's information
    """
    daily_acts = activity_map['daily']

    # Here, we'll just use the first instance's information
    # since the only variation should be the levels.
    daily_info = daily_acts[0]
    description = daily_info['activityDescription']
    skulls = daily_info['skulls']
    mods = [s['displayName'] for s in skulls]

    title = daily_info['activityName']

    daily_dict = {'title': title,
                  'description': description,
                  'mods': stringify_mods(mods),
                  'name': title,
    }
    return daily_dict

def process_crucible(activity_map):
    crucible_info = activity_map['crucible']
    description = crucible_info['activityDescription']

    title = crucible_info['activityName']

    crucible_dict = {'title': title,
                     'description': description,
                     'name': title,
    }

    return crucible_dict

def get_activity_details(activity_name):
    funcs = {
        'nightfall': process_nightfall,
        'daily': process_daily,
        'crucible': process_crucible,
        'heroic': process_heroic,
    }

    # TODO: Caching logic could probably go here.
    activity_json = fetch_activities()
    activities = process_activities(activity_json)

    return funcs[activity_name](activities)

if __name__ == '__main__':
    act_json = fetch_activities()
    activities = process_activities(act_json)
