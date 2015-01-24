from functools import partial
import requests
import bs4

template = "%(strike)s. Modifiers: %(mods)s"
event_url = 'http://destinytracker.com/destiny/events'

def get_mods(soup, index):
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


nightfall_mods = partial(get_mods, index=9)
heroic_mods = partial(get_mods, index=10)

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


if __name__ == '__main__':
    soup = get_soup()
    print nightfall_info(soup)
    print heroic_info(soup)
    print daily_info()
