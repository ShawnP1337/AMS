# AMS
Data Science Project for SDS 3386 

### Team Members
Alex Wyatt, Mariane Modena, Shawn Pokharel


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

![image](https://user-images.githubusercontent.com/52176354/196793360-fc1e043a-7251-4aa7-871f-22f407c25c61.png)

## Install The Needed Libraries 
Once the Virtual Enviornment is Activated install the Libraries we will be working with. 

```(venv) PS C:\Users\sanch\Desktop\Scraper\AMS> pip install pandas ```

```(venv) PS C:\Users\sanch\Desktop\Scraper\AMS> pip install snscrape ``` 

More Libraries may be need to installed later. 

## Run Scraper
```(venv) PS C:\Users\sanch\Desktop\Scraper\AMS> python scripts.py```

You should see a tweets.csv generated. 

![image](https://user-images.githubusercontent.com/52176354/196794425-4a6b906f-305f-4f59-9600-f7a599819af6.png)

Console Output Will Print a list of tweet contents. (Can be removed line 18/19)

## Jupiter Note BooK Data Analysis
Once you have the csv file. You can open Jupiter Notebook and Begin data analyzing! :grinning:

## Deactivate Virtual Env 
If you are looking to deactivate Virtual Enviornment
```(venv) PS C:\Users\sanch\Desktop\Scraper\AMS>deactivate```
