import requests
import json
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Set the bearer token
bearer_token = ""

# API endpoint to search for tweets
url = "https://api.twitter.com/2/tweets/search/recent?query=%23bitcoin&max_results=100"

# Use the bearer token for authentication
headers = {
    "Authorization": "Bearer " + bearer_token,
    "User-Agent": "My Twitter App"
}

# Make a GET request to the API
response = requests.get(url, headers=headers)

# Parse the response as JSON
tweets = json.loads(response.text)['data']

# Initialize SentimentIntensityAnalyzer
sentiment_analyzer = SentimentIntensityAnalyzer()

# Iterate through tweets and analyze sentiment
sentiments = []
for tweet in tweets:
    text = tweet['text']
    score = sentiment_analyzer.polarity_scores(text)['compound']
    sentiments.append((text, score))

# Sort sentiments by score
sentiments.sort(key=lambda x: x[1], reverse=True)

print("Top 5 most positive tweets:")
for text, score in sentiments[:5]:
    print(f"{text} - {score}")

print("\nTop 5 most negative tweets:")
for text, score in sentiments[-5:]:
    print(f"{text} - {score}")
