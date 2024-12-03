from textblob import TextBlob
from newspaper import Article

url = "https://abcnews.go.com/GMA/Travel/british-airways-christmas-dinner-flight-gift-wrapping/story?id=116405419"
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity  # -1 to 1 (Negative to Positive Sentiment)
print(sentiment)
