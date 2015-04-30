import json
import os

import pytest
import bungie

# Get the API response file once, since it won't change.
test_dir = os.path.dirname(os.path.realpath(__file__))
_api_file = open(test_dir + '/fixtures/full_response.json', 'r')
FULL_API_RESPONSE = json.load(_api_file)
API_RESPONSE = FULL_API_RESPONSE['Response']

@pytest.fixture(autouse=True)
def no_request_get(monkeypatch):
    # Set up a mock API response that will be present on all tests,
    # so we don't have to hit the network for testing.
    def mock_fetch_activities(url):
        return API_RESPONSE
    monkeypatch.setattr(bungie, 'fetch_activities', mock_fetch_activities)

def test_process_activities():
    api_response = bungie.fetch_activities('url')

    activities = bungie.process_activities(api_response)

    names = ('nightfall', 'crucible', 'daily', 'heroic')
    assert all(name in activities.keys() for name in names)
    assert all(activities[name] is not None for name in names)

def test_process_nightfall():
    api_response = bungie.fetch_activities('url')

    activities = bungie.process_activities(api_response)

    nf = bungie.process_nightfall(activities)

    keys = ('title', 'description', 'mods', 'name')
    assert all(key in nf.keys() for key in keys)
    assert 'Nightfall' in nf['title']
    assert 'Will of Crota' in nf['name']
    assert len(nf['mods']) == 5
    assert 'Void Burn' in nf['mods']
    assert 'Arc Burn' in nf['mods']
    assert 'Solar Burn' in nf['mods']


def test_process_heroic():
    api_response = bungie.fetch_activities('url')

    activities = bungie.process_activities(api_response)

    heroic = bungie.process_heroic(activities)

    keys = ('title', 'description', 'mods', 'name')
    assert all(key in heroic.keys() for key in keys)
    assert 'Heroic' in heroic['title']
    assert 'Will of Crota' in heroic['name']
    assert len(heroic['mods']) == 2
    assert 'Heroic' in heroic['mods']
    assert 'Solar Burn' in heroic['mods']

def test_process_daily():
    api_response = bungie.fetch_activities('url')

    activities = bungie.process_activities(api_response)

    daily = bungie.process_daily(activities)

    keys = ('title', 'description', 'mods')
    assert all(key in daily.keys() for key in keys)
    assert 'Siege of the Warmind' in daily['title']
    assert 'Siege of the Warmind' in daily['name']
    assert len(daily['mods']) == 2
    assert 'Heroic' in daily['mods']
    assert 'Angry' in daily['mods']

def test_process_crucible():
    api_response = bungie.fetch_activities('url')

    activities = bungie.process_activities(api_response)

    crucible = bungie.process_crucible(activities)

    keys = ('title', 'description', 'name')
    assert all(key in crucible.keys() for key in keys)
    assert "Executor's Challenge" in crucible['title']
    assert "Executor's Challenge" in crucible['name']
