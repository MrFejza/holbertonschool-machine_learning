#!/usr/bin/env python3

"""
Module for retrieving and displaying information about the first SpaceX launch
using the SpaceX API.
"""
import requests
from datetime import datetime

def get_first_launch():
    """Get first launch with all required details."""
    url = 'https://api.spacexdata.com/v4/launches'
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to fetch data from SpaceX API")
        return

    launches = response.json()
    if not launches:
        print("No launches found")
        return

    # Ensure all launches have the 'date_unix' field
    for launch in launches:
        if 'date_unix' not in launch:
            print("Error: Missing 'date_unix' field in one or more launches.")
            return

    # Sort launches by date_unix
    launches.sort(key=lambda x: x.get('date_unix', float('inf')))
    first_launch = launches[0]

    # Get rocket name
    rocket_id = first_launch['rocket']
    rocket_response = requests.get(f'https://api.spacexdata.com/v4/rockets/{rocket_id}')
    if rocket_response.status_code == 200:
        rocket_name = rocket_response.json().get('name', "Unknown Rocket")
    else:
        rocket_name = "Unknown Rocket"

    # Get launchpad name & locality
    launchpad_id = first_launch['launchpad']
    launchpad_response = requests.get(f'https://api.spacexdata.com/v4/launchpads/{launchpad_id}')
    if launchpad_response.status_code == 200:
        launchpad_data = launchpad_response.json()
        launchpad_name = launchpad_data.get('name', "Unknown Launchpad")
        launchpad_locality = launchpad_data.get('locality', "")
    else:
        launchpad_name = "Unknown Launchpad"
        launchpad_locality = ""

    launch_name = first_launch.get('name', "Unknown Launch")
    # Convert 'date_utc' to local time format
    launch_date_utc = first_launch.get('date_utc', "Unknown Date")
    try:
        launch_date = datetime.fromisoformat(launch_date_utc).strftime("%Y-%m-%dT%H:%M:%S%z")
    except ValueError:
        launch_date = "Unknown Date"

    # Print formatted result
    print(f"{launch_name} ({launch_date}) {rocket_name} - {launchpad_name} ({launchpad_locality})")

if __name__ == '__main__':
    get_first_launch()
