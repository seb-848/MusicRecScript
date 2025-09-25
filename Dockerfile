# FROM python
# WORKDIR /MusicRecommendScript
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# CMD ["python","MusicRecommendScript.py"]
# FROM python
# WORKDIR /MusicRecommendScript
# COPY . /MusicRecommendScript
# CMD ["python","MusicRecommendScript.py"]

FROM python:3.10
WORKDIR /MusicRecommendScript
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn
COPY . .
CMD ["gunicorn", "MusicRecommendScript:app", "-b", "0.0.0.0:5000"]