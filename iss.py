#!/usr/bin/env python

__author__ = 'Daniel S. Waite'

from datetime import datetime
import requests
import turtle
import time

def main():
    r = requests.get("http://api.open-notify.org/astros.json").json()

    print(f'There are {r.get("number")} astronauts on the ISS.')
    print(f'Their names are: \n')
    for names in r.get("people"):
        print(names.get("name"))
    print()

    coordinates = requests.get("http://api.open-notify.org/iss-now.json").json()
    latitude = float(coordinates.get("iss_position").get("latitude"))
    longitude = float(coordinates.get("iss_position").get("longitude"))

    backdrop = turtle.Screen()
    backdrop.bgpic("map.gif")

    try:
        p = requests.get("http://api.open-notify.org/iss-pass.json?lat=-86.158&lon=39.7684")
        p.raise_for_status()
    except requests.exceptions.HTTPError:
        print("\n\nTHE API IS DOWN\n\n")  

    passover = p.json
    
    # passover = {
    #     "message": "success",
    #     "request": {
    #     "latitude": 1234,
    #     "longitude": 5678, 
    #     "altitude": 5,
    #     "passes": 7,
    #     "datetime": 1545730073
    #     },
    #         "response": [{"risetime": 1545730073, "duration": "3 hours"}]
    #     }

    iss = turtle.Turtle()
    backdrop.setup(width=720, height=360)
    backdrop.setworldcoordinates(-180, -90, 180, 90)
    backdrop.register_shape("iss.gif")
    iss.shape("iss.gif")
    iss.penup()
    iss.goto(latitude, longitude)
    iss.write(time.ctime(coordinates.get("timestamp")), font=('Courier', 12, 'bold'), align='left')
    

    indianapolis = turtle.Turtle()
    indianapolis.shape("circle")
    indianapolis.fillcolor("yellow")
    indianapolis.penup()
    indianapolis.goto(-86.158, 39.7684)

    indianapolis.color("yellow") # <-- wrong
    indianapolis.write(time.ctime(passover.get("request").get("datetime")), font=('Courier', 12, 'bold'), align='left')

    # print(time.ctime(passover.get("request").get("datetime")))
    # print(time.ctime(coordinates.get("timestamp")))

    turtle.done()

if __name__ == '__main__':
    main()
