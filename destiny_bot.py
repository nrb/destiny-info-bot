from helga.plugins import command

from functions import xur_lookup
from scraper import nightfall_info, heroic_info, daily_info, crucible_info, get_soup

nf_help = 'Displays info on the current nightfall from destinytracker.com'

@command('nightfall', aliases=('nf',), help=nf_help)
def nightfall(client, channel, nick, message, cmd, args):
    soup = get_soup()
    return nightfall_info(soup)

hero_help = 'Displays info on the current heroic from destinytracker.com'
@command('heroic', aliases=('hero',), help=hero_help)
def heroic(client, channel, nick, message, cmd, args):
    soup = get_soup()
    return heroic_info(soup)

daily_help = 'Displays info on the current heroic daily from planetdestiny.com'
@command('daily', aliases=(), help=daily_help)
def daily(client, channel, nick, message, cmd, args):
    return daily_info()

crucible_help = 'Displays info on the current daily crucible mode form planetdestiny.com'
@command('crucible', aliases=(), help=crucible_help)
def crucible(client, channel, nick, message, cmd, args):
    return crucible_info()

@command('xur', aliases=(), help="Gives a URL for looking up Xur's inventory")
def xur(client, channel, nick, message, cmd, args):
    return xur_lookup()
