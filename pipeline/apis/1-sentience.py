#!/usr/bin/env python3
"""
Sentient Planets
"""
import requests

def sentientPlanets():
  planets = []
  base_url = 'https://swapi-api.hbtn.io/api/planets'
  while base_url is not None:
      response = requests.get(base_url)
      data = response.json()
      for planet in data['results']:
          residents = planet['residents']
          if residents:
              planets.append(planet['name'])
      base_url = data['next']
  return planets