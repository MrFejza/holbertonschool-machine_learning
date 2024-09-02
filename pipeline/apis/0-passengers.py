#!/usr/bin/env python3
#prototype
# do python prototype 

import requests

def availableShips(passengerCount):
    ships = []
    base_url = 'https://swapi-api.hbtn.io/api/starships'
    while base_url is not None:
        response = requests.get(base_url)
        data = response.json()
        for ship in data['results']:
            passengers = ship['passengers']
            if passengers.isnumeric() and int(passengers) >= passengerCount:
                ships.append(ship['name'])
        base_url = data['next']
    return ships