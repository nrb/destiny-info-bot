from helga.plugins import command

from scraper import nightfall_info, heroic_info

nf_help = 'Displays info on the current nightfall from destinytracker.com'

@command('nightfall', aliases=('nf',), help=nf_help)
def nightfall(client, channel, nick, message, cmd, args):
    return nightfall_info()

hero_help = 'Displays info on the current heroic from destinytracker.com'
@command('heroic', aliases=('hero',), help=hero_help)
def heroic(client, channel, nick, message, cmd, args):
    return heroic_info()

