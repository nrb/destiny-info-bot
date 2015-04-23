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


NIGHTFALL = 'nightfall'
WEEKLY_HEROIC = 'weekly heroic'

def weekly_lockout_event_info(soup, event):
    """:param soup: the document to search through
       :param event: the name of the event (should be either
                     ``NIGHTFALL`` or ``WEEKLY_HEROIC`` as defined in the
                     ``scraper`` module).
    """

    # FIXME: the next() call will raise if it doesn't find at least one node
    title = next(i for i in soup.select('div.activity-title')
                 if event in i.text.lower())
    root = title.findParent().findParent().findParent()
    return template % {
        'strike': title.findNextSibling().text,
        'mods': ', '.join(i.text for i in root.select('.tooltip-caption'))}


def nightfall_info(soup):
    return weekly_lockout_event_info(soup, NIGHTFALL)


def heroic_info(soup):
    return weekly_lockout_event_info(soup, WEEKLY_HEROIC)


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
    weekly_soup = get_soup('http://db.planetdestiny.com')
    print nightfall_info(weekly_soup)
    print heroic_info(weekly_soup)
    # soup = get_soup()
    # print daily_info()
    # print crucible_info()
    # print bounty_info('Vanguard')
    # print "---"
    # print bounty_info('Crucible')
    # print "---"
    # print bounty_info('Eris')
