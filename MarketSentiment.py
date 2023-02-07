import requests
import json
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Set the bearer token
bearer_token = "AAAAAAAAAAAAAAAAAAAAAHWvlgEAAAAAgBkcazXIQk2fExSSYNwgOxfuqk4%3Di3Kz8N5b5hQ9OZ1HabBWmVCdsZDedl5pGUpUoYjzJJ6XSqU9fu"

# API endpoint to search for tweets
url = "https://api.twitter.com/2/tweets/search/recent?query=%23Polygon&max_results=100"

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
    sentiments.append(score)

# Calculate the average sentiment score
average_sentiment = sum(sentiments) / len(sentiments)

# Print the overall market sentiment
if average_sentiment > 0:
    print("The market sentiment for Bitcoin is bullish with a score of ", average_sentiment)
else:
    print("The market sentiment for Bitcoin is bearish with a score of ", average_sentiment)
