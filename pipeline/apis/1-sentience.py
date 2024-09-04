#!/usr/bin/env python3
"""
Sentient Planets
"""
import requests

def is_sentient(species):
    # Check if the species is sentient based on classification or designation
    return species.get('classification') == 'sentient' or species.get('designation') == 'sentient'

def sentientPlanets():
    planets = set()  # Use a set to avoid duplicate planet names
    base_url = 'https://swapi-api.hbtn.io/api/species'
    
    while base_url is not None:
        response = requests.get(base_url)
        data = response.json()
        for species in data['results']:
            if is_sentient(species):
                homeworld_url = species.get('homeworld')
                if homeworld_url:
                    # Fetch the homeworld planet details
                    try:
                        planet_response = requests.get(homeworld_url)
                        planet_data = planet_response.json()
                        planets.add(planet_data['name'])
                    except requests.exceptions.RequestException as e:
                        print(f"Error fetching planet data: {e}")
        base_url = data['next']
    
    return list(planets)

# Test the function
if __name__ == "__main__":
    sentient_planets = sentientPlanets()
    for planet in sentient_planets:
        print(planet)
