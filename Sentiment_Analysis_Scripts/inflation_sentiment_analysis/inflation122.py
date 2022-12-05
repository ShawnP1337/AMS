import os
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import csv

path = "C:\\Users\\awyat049\\OneDrive\\Documents\\Coding\\2022_11_26_Cleaned_Twitter_Data\\inflation"

#change these to change files
start = 605
stop = 610

os.chdir(path)

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

all_filenames = []
with open('inflationfilelist.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        all_filenames.append(row[0])

#print(len(all_filenames))
#730

#Range is inclusive in python so range(3,6) prints 3,4,5
for f in range(start,stop):
    os.chdir(path)
    filename = all_filenames[f]
    data = pd.read_csv(filename)
    data = data.dropna(subset=["tweet"])
    tweetsArr = data['tweet'].to_numpy()
    list = []

    for tweet in tweetsArr:
        vs = getVaderSentimentScore(tweet)
        list.append(str(vs))

    data['Sentiment'] = list

    finalfile = filename + '_sentiment.csv'
    os.chdir("C:\\Users\\awyat049\\OneDrive\\Documents\\Coding\\2022_11_29_Final_Data_Full\\inflation_clean")
    data.to_csv(finalfile)