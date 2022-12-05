import pandas as pd
import os 
import matplotlib.pyplot as plt

outpath = "C:\\Users\\awyat049\\OneDrive\\Documents\\Coding\\Visualization\\inflation"
datapath = "C:\\Users\\awyat049\\OneDrive\\Documents\\Coding\\2022_11_29_Final_Data_Full"
os.chdir(datapath)

inflation = pd.read_csv("inflation_sentiment.csv")

inflation = inflation.drop(columns = ['username', 'location', 'profile bio', 'likes', 'retweets'])

os.chdir(outpath)

inflation.to_csv( "inflation_for_graphs.csv", index=False, encoding='utf-8-sig')