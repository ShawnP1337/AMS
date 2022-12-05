import os
import csv
import pandas as pd

readpath = "C:\\Users\\awyat049\\OneDrive\\Documents\\Coding\\2022_11_29_Final_Data_Full"
writepath = "D:\\Documents\\Coding\\Twitter_Scrape\\Sentiment_backup\\Removed Dupes"

os.chdir(readpath)

data = pd.read_csv('inflation_clean_all_tweets_sentiment.csv')
data = data.drop(columns = 'Unnamed: 0')

#print(data)
data.drop_duplicates(subset=None,inplace=True)
data.to_csv('inflation_sentiment.csv', index=False)

#read_file = open('affordable_housing_all_tweets_sentiment.csv', 'r', encoding = 'utf-8-sig')
#out_file = open('affordable_housing_sentiment.csv','w')

""" with open('foreign_buyer_ban_all_tweets_sentiment.csv', 'r', encoding = 'utf-8-sig') as read_file, open('foreign_buyer_ban_sentiment.csv','w', encoding = 'utf-8-sig') as out_file:
    seen = set() # set for fast O(1) amortized lookup
    for line in read_file:
        if line in seen: continue # skip duplicate

        seen.add(line)
        out_file.write(line)

out_file.close()
read_file.close() """
