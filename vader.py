from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import numpy as np

data = pd.read_csv("Freedom Convoy.csv")

tweetsArr = data['Tweet'].to_numpy()

analyzer = SentimentIntensityAnalyzer()

for tweet in tweetsArr:
    vs = analyzer.polarity_scores(tweet)
    print("{:-<65} {}".format(tweet, str(vs)))

