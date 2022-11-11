import snscrape.modules.twitter as sntwitter
import pandas as pd
import os
import threading
import time
from datetime import date, timedelta

# Allows us to automate datetime's for ease of use
# Return: a list of dates, each in an array where index zero is the datetime of the start of a 3 day period and index one is the datetime of the end of it
def iterateDate(start, end):
    count = 0
    for i in range(int((end - start).days)):
        count+=1
        if count%3 == 0:
            base = start + timedelta(i)
            yield [base, base + timedelta(days = 3)]


def scrapeIt(filename, searchPhrase, datestart, dateend):

    # Creating list to append tweet data to
    tweets_list1 = []
    tweetContentList = []

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(searchPhrase + ' since:' + datestart + ' until:' + dateend).get_items()):
        tweets_list1.append([tweet.date.strftime('%Y-%m-%d'), tweet.content, tweet.user.username,  tweet.user.location, tweet.user.description, tweet.likeCount, tweet.retweetCount])
        tweetContentList.append([tweet.content])
    
# Creating a dataframe from the tweets list above 

#Print Tweets Line By Line
#for elem in tweetContentList:
#    print(elem)

#Turn The Twitter Object List into a Pandas Dataframe
    tweets_df1 = pd.DataFrame(tweets_list1, columns=['Date', 'Tweet', 'Username', 'Location', 'Profile Bio', 'Likes', 'Retweets'])

    
    strf = os.getcwd() + "  :  " + filename
    print(strf)
    tweetsCSV = tweets_df1.to_csv(filename + '.csv', index=False)

def main():
    count = 0
    tasks = []
    # we gather all tweets three days at a time, running concurrently as out issue is with IO and this allows more IO requestion and should speed up processing
    for day in iterateDate(date(2016,10,26), date(2022,10,26)):

        tasks.append(threading.Thread(target=scrapeIt, args = ("Inflation" + str(day), "Increase of prices", day[0].strftime("%Y-%m-%d"), day[1].strftime("%Y-%m-%d"))))
        tasks[-1].start()
        count += 1
    
    for task in tasks:
        task.join()
        


if __name__ == "__main__":
    start_time = time.perf_counter()

    main()

    end_time = time.perf_counter()
    print(f"Elapsed run time: {end_time - start_time} seconds.")