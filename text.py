from textblob import TextBlob

with open("review.txt", "r") as f:
    text = f.read()

blob = TextBlob(text)
sentiment = blob.sentiment.polarity  # -1 to 1 (Negative to Positive Sentiment)
print(sentiment)
