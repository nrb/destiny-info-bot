from helga.plugins import command

from functions import bounty_lookup, crucible_lookup, daily_lookup
from functions import heroic_lookup, nightfall_lookup, xur_lookup
from scraper import VENDOR_NAMES

nf_help = 'Displays info on the current nightfall from destinytracker.com'

@command('nightfall', aliases=('nf',), help=nf_help)
def nightfall(client, channel, nick, message, cmd, args):
    return nightfall_lookup()

hero_help = 'Displays info on the current heroic from destinytracker.com'
@command('heroic', aliases=('hero',), help=hero_help)
def heroic(client, channel, nick, message, cmd, args):
    return heroic_lookup()

daily_help = 'Displays info on the current heroic daily from planetdestiny.com'
@command('daily', aliases=(), help=daily_help)
def daily(client, channel, nick, message, cmd, args):
    return daily_lookup()

crucible_help = 'Displays info on the current daily crucible mode form planetdestiny.com'
@command('crucible', aliases=(), help=crucible_help)
def crucible(client, channel, nick, message, cmd, args):
    return crucible_lookup()

@command('xur', aliases=(), help="Gives a URL for looking up Xur's inventory")
def xur(client, channel, nick, message, cmd, args):
    return xur_lookup()

valid_names = ' ,'.join(VENDOR_NAMES)
bounty_help = "Looks up the bounties for a given vendor. Valid names are: %s" % valid_names
@command('bounties', aliases=('b',), help=bounty_help)
def bounties(client, channel, nick, message, cmd, args):
    vendor_name = args[0]

    if vendor_name.title() not in VENDOR_NAMES:
        return "Invalid vendor. Valid names are: %s" % valid_names

    return bounty_lookup(vendor_name)
