from helga.plugins import command

from scraper import nightfall_info, heroic_info, get_soup

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
