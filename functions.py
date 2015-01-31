import datetime

from pytz import timezone


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


if __name__ == '__main__':
    print xur_lookup()
