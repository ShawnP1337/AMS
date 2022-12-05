import pandas as pd
import os 
import matplotlib.pyplot as plt

datapath = "C:\\Users\\awyat049\\OneDrive\\Documents\\Coding\\Visualization\\inflation"
os.chdir(datapath)

inflation = pd.read_csv("inflation_DateTweetSent.csv")

def columns(df, file):
    
    # the compound score column
    current = 0.0
    first = ""
    second = ""
    score = []
   # print(df.iloc[0]['Sentiment'])
    
    for i in range(0,len(df['Sentiment'])):
        first = (df.iloc[i]['Sentiment']).split('compound')[1]
        second = (first.split('}'))[0]
        score.append( float((second.split(':'))[1]))
    
    df['compound_score'] = score
    #print(len(score))
    #print(len(df['Sentiment']))
    """ for j in score:
        print(j) """


    """ df[['compound']] = df['Sentiment'].str.split('compound', expand=True)[[1]]
    df[['compound_score']] = df['compound'].str.split('}', expand=True)[[0]]
    df[['compound_score']] = df['compound_score'].str.split(':', expand=True)[[1]].astype('float')
    df = df.drop(columns=['compound']) """
    
    # the period column (only the year and month from the date, it will be useful for time series)
    
    df['period'] = df['date'].str[:-3]

    df = df.drop(columns = 'date')
    
    # the topic column will also be useful for the graphs 
    
    term = file.replace('_DateTweetSent.csv', '')
    df['topic'] = term
    
    return df

inflation = columns(inflation, "inflation_DateTweetSent.csv")

inflation.to_csv( "inflation_pre_graphs.csv", index=False, encoding='utf-8-sig')