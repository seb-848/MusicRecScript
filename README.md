# Last.fm Music Recommendation
Python + Docker project that calls Last.fm API to recommend similar artists

docker build -t music-recommender .

EXPLICIT KEY
docker run -it --rm -e LASTFM_API_KEY="your_key_here" music-recommender

ENV FILE
docker run -it --rm --env-file .env music-recommender


# Last.fm lastfm-flask

build image
docker build -t lastfm-flask .

explicit key
docker run -p 5000:5000 -e LASTFM_API_KEY="your_actual_key" lastfm-flask

env file
docker run -p 5000:5000 --env-file .env lastfm-flask

## Link
http://localhost:5000/similar?artist=artist
but type in artist