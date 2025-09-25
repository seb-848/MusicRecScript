from flask import Flask, request, jsonify
import requests, os

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")
BASE_URL = 'http://ws.audioscrobbler.com/2.0'

@app.route("/similar")
def  similar():
    artist = request.args.get("artist")
    if not artist:
        return jsonify({"error": "Provide artist name"}), 400

    # Call the Last.fm API
    r = requests.get(BASE_URL,
                     params={
                        "method": "artist.getSimilar",
                        "artist": artist,
                        "api_key": API_KEY,
                        "format": "json",
                        "limit": 5
                     })
    
    if r.status_code != 200:
        return jsonify({"Error": "Failed to fetch data"}), 500
    
    data = r.json()

    try:
        artists = [a["name"] for a in data["similarartists"]["artist"]]
    except KeyError:
        return jsonify({"Error": "Artist not foun"}), 404
    
    return jsonify({"artist": artist, "similar_artists": artists})