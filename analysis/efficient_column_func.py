import pandas as pd
import os 
import matplotlib.pyplot as plt

datapath = "C:\\Users\\awyat049\\OneDrive\\Documents\\Coding\\2022_11_29_Final_Data_Full"
os.chdir(datapath)

filename = "increase_price_housing_sentiment.csv"

term = pd.read_csv(filename)

def columns(df, file):
    
    # the compound score column
    first = ""
    second = ""
    score = []
    pos_sent = [0]*len(df['Sentiment'])
    neg_sent = [0]*len(df['Sentiment'])
    neut_sent = [0]*len(df['Sentiment'])
   # print(df.iloc[0]['Sentiment'])
    
    for i in range(0,len(df['Sentiment'])):
        first = (df.iloc[i]['Sentiment']).split('compound')[1]
        second = (first.split('}'))[0]
        score.append( float((second.split(':'))[1]))

        if 'Positive' in df.iloc[i]['Sentiment']:
            pos_sent[i] = 1
        elif 'Negative' in df.iloc[i]['Sentiment']:
            neg_sent[i] = 1
        else:
            neut_sent[i] = 1

    
    df['compound_score'] = score
    
    
    # the period column (only the year and month from the date, it will be useful for time series)
    
    df['period'] = df['date'].str[:-3]

    df = df.drop(columns = 'date')
    
    # the topic column will also be useful for the graphs 
    
    term = file.replace('_sentiment.csv', '')
    df['topic'] = term

    df['Positive Sentiment'] = pos_sent
    df['Neutral Sentiment'] = neg_sent
    df['Negative Sentiment'] = neut_sent

    
    
    return df

term = columns(term, filename)

term.to_csv( term.iloc[1]['topic'] + "columned.csv", index=False, encoding='utf-8-sig')