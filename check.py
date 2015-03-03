#!/usr/bin/env python

import sys

from functions import daily_lookup,  heroic_lookup, nightfall_lookup
from functions import bounty_lookup, crucible_lookup, VENDOR_NAMES

def check_bounties():
    bounties = []
    for name in VENDOR_NAMES:
        bounties.extend([name, '---'])
        bounties.append(bounty_lookup(name))
    return '\n'.join(bounties)


def main(command):
    cmd_map = {
        'daily': daily_lookup,
        'heroic': heroic_lookup,
        'nightfall': nightfall_lookup,
        'crucible': crucible_lookup,
        'bounties': check_bounties,

    }

    if command not in cmd_map.keys():
        return "%s was not a valid command" % command

    func = cmd_map[command]
    return func()


if __name__ == '__main__':
    command = sys.argv[1]
    print main(command)
