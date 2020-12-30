#!/usr/bin/env python

# List of astronauts
# http://api.open-notify.org/astros.json
# http://api.open-notify.org/iss-now.json
# http://api.open-notify.org/iss-pass.json

__author__ = 'Daniel S. Waite'

import requests

# write a Python program to obtain a list of the 
# astronauts who are currently in space. 
# Print their full names, the spacecraft they are currently on board, 
# and the total number of astronauts in space.

def main():
    r = requests.get("http://api.open-notify.org/astros.json").json()

    print(f'There are {r.get("number")} astronauts on the ISS.')
    print(f'Their names are: \n')
    for names in r.get("people"):
        print(names.get("name"))
    print()


if __name__ == '__main__':
    main()
