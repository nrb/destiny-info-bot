from functools import partial
import requests
import bs4


event_url = 'http://destinytracker.com/destiny/events'

class ScrapeError(Exception):
    pass

def get_soup(event_url=event_url):
    response = requests.get(event_url)
    html = response.text

    soup = bs4.BeautifulSoup(response.text)
    return soup


def strike_title(soup):
    title = soup.select('h4.media-heading')[-1].text
    return title


NIGHTFALL = 'nightfall'
WEEKLY_HEROIC = 'weekly heroic'

VENDOR_NAMES = [
    'eris',
    'crucible',
    'vanguard',
]

def find_tables(vendor):
    soup = get_soup("http://db.planetdestiny.com/events")
    headers = soup.select('h3')
    target_index = None
    for index, header in enumerate(headers):
        if vendor in header.text.lower():
            target_index = index
            break

    table = soup.select('table')[target_index]

    return table

def read_bounty_tables(vendor):
    vendor = vendor.lower()
    table = find_tables(vendor)

    # The first row is the heading
    rows = table.select('tr')[1:]

    bounties = {}
    for row in rows:
        cells = row.select('td')
        name = cells[0].select('a')[0].text
        name = name.strip()

        desc = cells[1].text.strip()

        bounties[name] = desc

    return bounties
