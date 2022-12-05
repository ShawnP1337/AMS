import snscrape.modules.twitter as sntwitter
import pandas as pd
import os

# Creating list to append tweet data to
tweets_list1 = []
tweetContentList = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('housing crisis since:2021-01-01 until:2022-09-21').get_items()):
    if i>100000:
        break
    tweets_list1.append([tweet.date.strftime('%Y-%m-%d'), tweet.content, tweet.user.username,  tweet.user.location, tweet.user.description, tweet.likeCount, tweet.retweetCount])
    tweetContentList.append([tweet.content])
    
# Creating a dataframe from the tweets list above 

#Print Tweets Line By Line
#for elem in tweetContentList:
#    print(elem)

#Turn The Twitter Object List into a Pandas Dataframe
tweets_df1 = pd.DataFrame(tweets_list1, columns=['Date', 'Tweet', 'Username', 'Location', 'Profile Bio', 'Likes', 'Retweets'])

print(os.getcwd())
tweetsCSV = tweets_df1.to_csv('house_tweets2.csv', index=False)
