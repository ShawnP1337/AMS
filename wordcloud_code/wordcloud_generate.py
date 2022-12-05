import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from wordcloud import STOPWORDS

outpath = "C:\\Users\\awyat049\\OneDrive\\Documents\\Coding\\Visualization"
filepath = "C:\\Users\\awyat049\\OneDrive\\Documents\\Coding\\Visualization\\tweettxt\\inflation_tweets_no_term.txt"

text =""

with open(filepath, 'r', encoding = 'utf-8-sig') as t:
    text = t.readlines()

text = str(text)
t.close()

stop_words = ["n'"] + list(STOPWORDS)


#print(df.tweet)

os.chdir(outpath)

wordcloud = WordCloud(max_words = 40, stopwords = stop_words, collocations = False, background_color = 'white').generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()