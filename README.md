# AMS Senitment Analysis
Data Science Project for SDS 3386 

### Team Members
Alex Wyatt, Mariane Modena, Shawn Pokharel

# Single Process Scraper
## Setup the Scraper
First Clone this repo to the desired path 

``` C:\Users\*Desired Path*> git clone https://github.com/ShawnP1337/AMS.git```

## Install a Virtual Enviornment (venv) in the same path as the AMS repo

``` C:\Users\*Path to the Virtual Enviornment*> python -m venv venv  ```

Once the Virtual Enviornment is Created, directory should look something like this

![image](https://user-images.githubusercontent.com/52176354/196791497-36507ff7-d5d0-43a1-90b0-0b415c486f6c.png)

## Active the Virtual Enviornment

``` C:\Users\*Desired Path*>.\.venv\Scripts\activate ```   

When your virual enviornment is activated, your command line should look something like this. 

* to activate try ``` source Scripts/activate ```

![image](https://user-images.githubusercontent.com/52176354/196793360-fc1e043a-7251-4aa7-871f-22f407c25c61.png)

## Install The Needed Libraries 
Once the Virtual Enviornment is Activated install the Libraries we will be working with. 

```(venv) PS C:\Users\sanch\Desktop\Scraper\AMS> pip install pandas ```

```(venv) PS C:\Users\sanch\Desktop\Scraper\AMS> pip install snscrape ``` 

More Libraries may be need to installed later. 

## Run Scraper
```(venv) PS C:\Users\sanch\Desktop\Scraper\AMS> python scraper.py```

You should see a tweets.csv generated. 

![image](https://user-images.githubusercontent.com/52176354/196794425-4a6b906f-305f-4f59-9600-f7a599819af6.png)

Console Output Will Print a list of tweet contents. (Can be removed line 18/19)

## Jupiter Note BooK Data Analysis
Once you have the csv file. You can open Jupiter Notebook and Begin data analyzing! :grinning:

## Deactivate Virtual Env 
If you are looking to deactivate Virtual Enviornment
```(venv) PS C:\Users\sanch\Desktop\Scraper\AMS>deactivate```

# Snscraper
Link to Scraper Module 
https://github.com/JustAnotherArchivist/snscrape

## Attributes we can scrape from Tweet Object 
Attribute Description leftt blank if purpose unknown

```
url: Permalink pointing to tweet location
date: Date tweet was created
content: Text content of tweet
renderedContent: Appears to also be text content of tweet
id: Id of tweet
user: User object containing the following data: usemame, displayname, id, description, descriptionUr, verified, created, followersCount, friendsCount,
statusesCount, favouritesCount, listedCount, mediaCount, location, protected, linkUr, profilelmageUr|, profileBannerUrl
outlinks
tcooutlinks
‘replyCount: Count of replies
retweetCount: Count of retweets
ikeCount: Count of likes
quoteCount: Count of users that quoted the tweet and replied
conversationid: Appears to be the same as tweet Id
lang: Machine generated, assumed language of tweet
source: Where tweet was posted from, ex: IPhone, Android, etc.
media: Media object, containing previewUr, full, and type.
retweetedTweet: Ifis a retweet, id of original tweet
quotedTweet: IFis a quoted tweet, id of original tweet
mentionedUsers: User objects of any mentioned user in tweet
```
# Parallel Processing Scraper C++ 
See twitter_data_cleaning_code_c++

# Vader Setniment Analysis
https://github.com/cjhutto/vaderSentiment

# Panel Dashboard
https://ams-panel-dashboard.ue.r.appspot.com/app

## To run locally 
Download repo, open terminal, go into repo directory on terminal and run ```panel serve app ```
Should serve on localhost
![image](https://user-images.githubusercontent.com/52176354/206077365-97495d8a-b258-4e36-8f49-e91f9dfe4636.png)
