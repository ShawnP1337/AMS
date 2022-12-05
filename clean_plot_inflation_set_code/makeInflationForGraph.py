import pandas as pd
import os 
import matplotlib.pyplot as plt

datapath = "C:\\Users\\awyat049\\OneDrive\\Documents\\Coding\\Visualization\\inflation"
os.chdir(datapath)

inflation = pd.read_csv("inflation_pre_graphs.csv")

inflation_g = inflation.groupby('period').agg({'compound_score': 'mean', 'topic': 'first'}).reset_index()

inflation_g.to_csv( "inflation_for_graphs.csv", index=False, encoding='utf-8-sig')