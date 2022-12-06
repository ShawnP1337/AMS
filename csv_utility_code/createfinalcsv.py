import pandas as pd
import os 

def Pos(x):
    if 'Positive' in x:
        return 1
    else:
        return 0
def Neg(x):
    if 'Negative' in x:
        return 1
    else:
        return 0
def Neu(x):
    if 'Neutral' in x:
        return 1
    else:
        return 0

def columns(df, file):
    
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])
    
    # the compound score column
    
    df[['compound']] = df['Sentiment'].str.split('compound', expand=True)[[1]]
    df[['compound_score']] = df['compound'].str.split('}', expand=True)[[0]]
    df[['compound_score']] = df['compound_score'].str.split(':', expand=True)[[1]].astype('float')
    df = df.drop(columns=['compound'])
    
    # the period column (only the year and month from the date, it will be useful for time series)
    
    df['period'] = df['date'].str[:-3]
    
    # the topic column will also be useful for the graphs 
    
    term = file.replace('_sentiment.csv', '')
    df['topic'] = term
    
    # Iterating over one column - `f` is some function that processes your data
    df['Positive Sentiment'] = [Pos(x) for x in df['Sentiment']]
    df['Neutral Sentiment'] = [Neu(x) for x in df['Sentiment']]
    df['Negative Sentiment'] = [Neg(x) for x in df['Sentiment']]

    
    return df



path = "C:\\Users\\awyat049\\OneDrive\\Documents\\Coding\\2022_12_05_Final_Data_ComboScore"


readpath= "C:\\Users\\awyat049\\OneDrive\\Documents\\Coding\\2022_11_29_Final_Data_Full\\"
os.chdir(readpath)

filename = "standard_of_living_sentiment.csv"

filepath = readpath + filename

data = pd.read_csv(filepath)

os.chdir(path)

data = columns(data, filename)

data.to_csv(filename, index=False, encoding='utf-8-sig')
