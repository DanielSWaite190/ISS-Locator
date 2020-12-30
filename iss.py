#!/usr/bin/env python

# http://api.open-notify.org/astros.json
# http://api.open-notify.org/iss-now.json
# http://api.open-notify.org/iss-pass.json

__author__ = 'Daniel S. Waite'

import requests
import turtle

def main():
    r = requests.get("http://api.open-notify.org/astros.json").json()

    print(f'There are {r.get("number")} astronauts on the ISS.')
    print(f'Their names are: \n')
    for names in r.get("people"):
        print(names.get("name"))
    print()

    coordinates = requests.get("http://api.open-notify.org/iss-now.json").json().get("iss_position")
    latitude = float(coordinates.get("latitude"))
    longitude = float(coordinates.get("longitude"))


    backdrop = turtle.Screen()
    backdrop.bgpic("map.gif")

    iss = turtle.Turtle()
    backdrop.register_shape("iss.gif")
    iss.shape("iss.gif")
    iss.penup()
    iss.goto(latitude, longitude)
    turtle.done()
    

if __name__ == '__main__':
    main()
