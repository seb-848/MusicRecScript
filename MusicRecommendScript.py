from flask import Flask, request, jsonify, render_template
import requests, os

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")
BASE_URL = 'http://ws.audioscrobbler.com/2.0'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def  search():
    artist = request.args.get("artist")
    if not artist:
        return "Provide artist name.", 400

    # Call the Last.fm API
    r = requests.get(BASE_URL,
                     params={
                        "method": "artist.getSimilar",
                        "artist": artist,
                        "api_key": API_KEY,
                        "format": "json",
                        "limit": 10
                     })
    
    data = r.json()

    try:
        artists = [a["name"] for a in data["similarartists"]["artist"]]
    except KeyError:
        return f"No similar artists found for '{artist}'.", 404
    
    return render_template("results.html", artist=artist, artists=artists)