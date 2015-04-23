from functools import partial
import requests
import bs4


template = "%(strike)s. Modifiers: %(mods)s"
event_url = 'http://destinytracker.com/destiny/events'

class ScrapeError(Exception):
    pass


def find_term(soup, term):
    lists = soup.select('ul')
    for idx, ul in enumerate(lists):
        if term in ul.text:
            return idx
    return None

def get_mods(soup, term):
    index = find_term(soup, term)
    if index is None:
        return ''

    mod_list = soup.select('ul')[index]

    modifiers = [li.text for li in mod_list.select('li')]
    modifiers = ', '.join(modifiers)

    return modifiers


def get_soup(event_url=event_url):
    response = requests.get(event_url)
    html = response.text

    soup = bs4.BeautifulSoup(response.text)
    return soup


def strike_title(soup):
    title = soup.select('h4.media-heading')[-1].text
    return title


nightfall_mods = partial(get_mods, term='Nightfall')
heroic_mods = partial(get_mods, term='Heroic')

def nightfall_info(soup):
    return template % {'strike': strike_title(soup),
                       'mods': nightfall_mods(soup)}


def heroic_info(soup):
    return template % {'strike': strike_title(soup),
                       'mods': heroic_mods(soup)}


def daily_info():
    soup = get_soup("http://db.planetdestiny.com/events")

    title = soup.select('div.activity-title')[0].text
    title = title.strip()

    mod_list = soup.select('div.tooltip-caption')[0:2]
    modifiers = [div.text for div in mod_list]
    modifiers = ', '.join(modifiers)

    return template % {'strike': title, 'mods': modifiers}


def crucible_info():
    soup = get_soup("http://db.planetdestiny.com/events")

    act_titles = soup.select('div.activity-title')
    mode_title = act_titles[1].text.strip()

    return "Daily Crucible mode: %s" % mode_title


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


if __name__ == '__main__':
    #soup = get_soup()
    #print nightfall_info(soup)
    #print heroic_info(soup)
    #print daily_info()
    #print crucible_info()
    print bounty_info('Vanguard')
    print "---"
    print bounty_info('Crucible')
    print "---"
    print bounty_info('Eris')
