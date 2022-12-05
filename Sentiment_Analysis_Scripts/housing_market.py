import os
import pandas as pd
import glob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

path = "C:\\Users\\awyat049\\OneDrive\\Documents\\Coding\\2022_11_26_Cleaned_Twitter_Data\\housing_market"

os.chdir(path)

shortpath = path[:76]

#print(shortpath)

filename = path[76:]

#print(filename)

def calculateCompoundSentiment(sentiment_score):
    # decide sentiment as positive, negative and neutral
    if sentiment_score['compound'] >= 0.05 :
        return "Positive"
 
    elif sentiment_score['compound'] <= -0.05 :
        return "Negative"
 
    else :
        return "Neutral"


def getVaderSentimentScore(sentence):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(sentence)
    compoundSentiment = calculateCompoundSentiment(sentiment_score)
    return sentiment_score, compoundSentiment

extension = 'csv'
#count = 0
newname = filename + "_all_tweets.csv"
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
combined_csv = combined_csv.dropna(subset=["tweet"])
combined_csv.to_csv( newname, index=False, encoding='utf-8-sig')
combined_csv = None

newpath = shortpath + newname
#print(newpath)

data = pd.read_csv(newname)

tweetsArr = data['tweet'].to_numpy()
list = []
for tweet in tweetsArr:
    #print(count)
    #count = count + 1
    vs = getVaderSentimentScore(tweet)
    list.append(str(vs))

data['Sentiment'] = list

finalfile = filename + '_all_tweets_sentiment'
data.to_csv(finalfile)