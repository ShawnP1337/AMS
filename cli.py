import os
#Example of CLI Commands for snscrape  

#Scrape 100 recent tweets from elon musk and putput to a json file 
os.system("snscrape --jsonl --max-results 100 twitter-search 'from:elonmusk'> user-tweets.json")

#Scrape 500 tweets about housing crisis based on date conditions
os.system("snscrape --jsonl --progress --max-results 500 --since 2020-06-01 twitter-search 'Housing Crisis until:2020-07-31 ' > text-query-tweets.json")

#Scrape x number of tweets based on hashtag
os.system("snscrape --jsonl --max-results 100 twitter-hashtag capitalism > capitalism.json")

#Scrape x number of HISTORICAL tweets based on hashtag
os.system("snscrape --jsonl --max-results 100 --since 2020-06-01 twitter-hashtag 'capitalism until:2020-07-31 ' > capitalism.json")

# Information about Snscrape parameters. 
# https://betterprogramming.pub/how-to-scrape-tweets-with-snscrape-90124ed006af

"""
Snsscrape CLI Usuage 
usage: snscrape [-h] [--version] [--citation] [-v] [--dump-locals] [--retry N] [-n N] [-f FORMAT | --jsonl]
                [--with-entity] [--since DATETIME] [--progress]
                SCRAPER ...

options:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  --citation            Display recommended citation information and exit (default: None)
  -v, --verbose, --verbosity
                        Increase output verbosity (default: 0)
  --dump-locals         Dump local variables on serious log messages (warnings or higher) (default: False)
  --retry N, --retries N
                        When the connection fails or the server returns an unexpected response, retry up to N times
                        with an exponential backoff (default: 3)
  -n N, --max-results N
                        Only return the first N results (default: None)
  -f FORMAT, --format FORMAT
                        Output format (default: None)
  --jsonl               Output JSONL (default: False)
  --with-entity         Include the entity (e.g. user, channel) as the first output item (default: False)
  --since DATETIME      Only return results newer than DATETIME (default: None)
  --progress            Report progress on stderr (default: False)

scrapers:
  SCRAPER
    facebook-community
    facebook-group
    facebook-user
    instagram-hashtag
    instagram-location
    instagram-user
    mastodon-profile
    mastodon-toot
    reddit-search
    reddit-submission
    reddit-subreddit
    reddit-user
    telegram-channel
    twitter-hashtag
    twitter-list-posts
    twitter-profile
    twitter-search
    twitter-trends
    twitter-tweet
    twitter-user
    vkontakte-user
    weibo-user
 """