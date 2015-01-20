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

def get_soup(event_url):
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

if __name__ == '__main__':
    soup = get_soup(event_url)
    print nightfall_info(soup)
    print heroic_info(soup)
