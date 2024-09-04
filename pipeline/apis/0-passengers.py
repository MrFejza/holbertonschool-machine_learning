#!/usr/bin/env python3
"""
Create a method that returns the list of ships that can hold a given number
of passengers
"""

import requests

def availableShips(passengerCount):
    """
    Returns the list of ships that can hold a given number of passengers
    :param passengerCount: number of passengers
    :return: If no ship available, return an empty list
    """
    url = "https://swapi-api.hbtn.io/api/starships/"
    ships = []
    
    while url:
        response = requests.get(url)
        data = response.json()
        results = data.get("results", [])
        
        for res in results:
            passengers = res.get("passengers", "0").replace(',', '')
            if passengers.lower() not in ['n/a', 'unknown']:
                try:
                    if int(passengers) >= passengerCount:
                        ships.append(res["name"])
                except ValueError:
                    # Handle case where passengers value is not a valid integer
                    continue
        
        url = data.get("next")
    
    return ships
