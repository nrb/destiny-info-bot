#!/usr/bin/env python

import sys

from functions import daily_lookup,  heroic_lookup, nightfall_lookup

def main(command):
    if command not in ('nightfall', 'heroic', 'daily'):
        return "%s was not a valid command" % command

    cmd_map = {
        'daily': daily_lookup,
        'heroic': heroic_lookup,
        'nightfall': nightfall_lookup,
    }

    func = cmd_map[command]
    return func()


if __name__ == '__main__':
    command = sys.argv[1]
    print main(command)
