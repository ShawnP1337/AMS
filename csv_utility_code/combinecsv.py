import os
import pandas as pd
import glob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

path = "C:\\Users\\awyat049\\OneDrive\\Documents\\Coding\\2022_11_29_Final_Data_Full\\inflation_clean"

os.chdir(path)

filename = path[71:]

#print(filename)


extension = 'csv'
#count = 0
newname = filename + "_all_tweets_sentiment.csv"
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
combined_csv.to_csv( newname, index=False, encoding='utf-8-sig')
combined_csv = None