import pandas as pd
import os 
import altair as alt

datapath = "C:\\Users\\awyat049\\OneDrive\\Documents\\Coding\\Visualization\\inflation"
os.chdir(datapath)

inflation = pd.read_csv("inflation_for_graphs.csv")

alt.Chart(inflation, title='Average global score sentiment over the months (2016-2022)').mark_line().encode(
    x = alt.X('period:O', axis=alt.Axis(title='Time')),
    y = alt.Y('compound_score', axis=alt.Axis(title='Average compound sentiment score'), scale=alt.Scale(domain=[-.5,.5])),
    color=alt.Color('topic:N')
).properties(width=800)

