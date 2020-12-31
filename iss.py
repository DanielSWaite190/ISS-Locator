#!/usr/bin/env python

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
    backdrop.setup(width=720, height=360)
    backdrop.setworldcoordinates(-180, -90, 180, 90)
    backdrop.register_shape("iss.gif")
    iss.shape("iss.gif")
    iss.penup()
    iss.goto(latitude, longitude)
    

    indianapolis = turtle.Turtle()
    indianapolis.shape("circle")
    indianapolis.fillcolor("yellow")
    indianapolis.penup()
    indianapolis.goto(-86.158, 39.7684)

    turtle.done()

    # http://api.open-notify.org/iss-pass.json?=36
    # http://api.open-notify.org/iss-pass.json

if __name__ == '__main__':
    main()
