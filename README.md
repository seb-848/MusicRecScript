#Last.fm Music Recommendation
Python + Docker project that calls Last.fm API to recommend similar artists

docker build -t music-recommender .

EXPLICIT KEY
docker run -it --rm -e LASTFM_API_KEY="your_key_here" music-recommender

ENV FILE
docker run -it --rm --env-file .env music-recommender