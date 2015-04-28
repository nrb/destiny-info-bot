import datetime

from pytz import timezone

import caching as cache

from scraper import read_bounty_tables, ScrapeError, VENDOR_NAMES
from scraper import nightfall_info, heroic_info, daily_info, crucible_info, get_soup

VALID_SYSTEMS = ('ps', 'xbox')


def guardian_lookup(system, name):
    if system not in VALID_SYSTEMS:
        return '%s is not a valid system' % system
    link_template = 'http://destinytracker.com/destiny/overview/%(system)s/%(name)s'

    return link_template % {'system': system, 'name': name}

def xur_lookup():
    url_pattern = "http://www.vg247.com/%(year)s/%(month)s/%(friday)s/destiny-xur-location-and-inventory-for-%(month_name)s-%(friday)s-%(saturday)s"
    pacific = timezone('US/Pacific')
    today = datetime.datetime.today()

    pac_day = pacific.localize(today)

    day_name = pac_day.strftime('%A')

    if day_name not in ('Friday', 'Saturday'):
        return "Sorry, Xur isn't present right now."

    if day_name == 'Friday':
        friday = pac_day.day
        saturday = (pac_day + datetime.timedelta(days=1)).day
    elif day_name == 'Saturday':
        saturday = pac_day.day
        friday = (pac_day - datetime.timedelta(days=1)).day
    else:
        return "Something went wrong with the date math. I think today is %s" % day_name


    year = pac_day.year
    month = pac_day.month
    month_name = pac_day.strftime('%B')
    month_name = month_name.lower()

    url = url_pattern % {'year': year, 'month': month,
                         'month_name': month_name,
                         'friday': friday, 'saturday': saturday
                        }
    return url


def bounty_lookup(vendor):
    key = '%s-bounties' % vendor
    val = cache.read(key)
    if val is not None:
        return val

    try:
        bounties = read_bounty_tables(vendor)
    except ScrapeError as e:
        return e

    bounty_template = '%(name)s - %(desc)s'

    bounty_output = []
    for name, desc in bounties.items():
        line = bounty_template % {'name': name, 'desc': desc}
        bounty_output.append(line)

    out = '\n'.join(bounty_output)

    expiry = datetime.datetime.now() + datetime.timedelta(hours=1)

    cache.write(key, out, expiry)

    return out


def nightfall_lookup():
    val = cache.read('nightfall')
    if val is not None:
        return val

    soup = get_soup('http://db.planetdestiny.com')
    val = nightfall_info(soup)
    expiry = datetime.datetime.now() + datetime.timedelta(hours=1)

    cache.write('nightfall', val, expiry)

    return val


def heroic_lookup():
    val = cache.read('heroic')
    if val is not None:
        return val

    soup = get_soup('http://db.planetdestiny.com')
    val = heroic_info(soup)
    expiry = datetime.datetime.now() + datetime.timedelta(hours=1)

    cache.write('heroic', val, expiry)

    return val


def daily_lookup():
    val = cache.read('daily')
    if val is not None:
        return val

    val = daily_info()
    expiry = datetime.datetime.now() + datetime.timedelta(hours=1)

    cache.write('daily', val, expiry)

    return val


def crucible_lookup():
    val = cache.read('crucible')

    if val is not None:
        return val

    val = crucible_info()
    expiry = datetime.datetime.now() + datetime.timedelta(hours=1)

    cache.write('crucible', val, expiry)

    return val

if __name__ == '__main__':
    #print xur_lookup()
    print bounties('bad')
    print "----"
    print bounties('Eris')
    print "----"
    print bounties('Vanguard')

