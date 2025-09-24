import os
import requests

from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv("API_KEY")
BASE_URL = 'http://ws.audioscrobbler.com/2.0'

artist = input("Enter an artist name: ")

params = {
    "method": "artist.getSimilar",
    "artist": artist,
    "api_key": API_KEY,
    "format": "json",
    "limit": 5
}

# Send http GET request
response = requests.get(BASE_URL, params = params)

# Convert JSON -> Python dict
data = response.json()

if response.status_code != 200:
    print("Error:", response.status_code)
elif "similarartists" not in data:
    print("No results. Check spelling or try another artist.")
else:
    print("\nArtists similar to ", artist, ": ")
    for a in data['similarartists']['artist']:
        print("",a['name'])
