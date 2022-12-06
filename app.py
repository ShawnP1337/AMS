import panel as pn
from panel.interact import interact
import hvplot.pandas
import pandas as pd


df_mean_compound_score = pd.read_csv("https://storage.googleapis.com/sentiment_bucket_ams/AMS_Twitter_Data/output.csv")

symbols = list(df_mean_compound_score.topic.unique())

#create widget 
select1 = pn.widgets.Select(name='Select', options=symbols)

#creat function that works with widget
def create_plot(symbol):
    return df_mean_compound_score[df_mean_compound_score['topic']==symbol].hvplot('period','compound_score', rot=90, width=1300, height=700, title= "Average Sentiment Score per month [2016-2022]", xlabel="Period (Month)", ylabel="Mean Compound Sentiment Score")
#combine widget and function
interact = pn.bind(create_plot, symbol=select1)

#create widget 
select2 = pn.widgets.Select(name='Select', options=symbols)


def create_plot(symbol):
    return df_mean_compound_score[df_mean_compound_score['topic']==symbol].hvplot('period',['likes','retweets'], width=1600, height=700, rot=90,title= "Total Social Engagements per month [2016-2022]", xlabel="Period (Month)", ylabel="Total number of Engagements")

interact2 = pn.bind(create_plot, symbol=select2)

#create widget 
select3 = pn.widgets.Select(name='Select', options=symbols)


def create_plot(symbol):
    return df_mean_compound_score[df_mean_compound_score['topic']==symbol].hvplot.bar('period',['Positive Sentiment','Negative Sentiment','Neutral Sentiment'], stacked=True, rot=90, width=1600, height=1000, title="Total number of Positive/Negative/Neutral Tweets per month [2016-2022]", xlabel="Period (Month)", ylabel="Total number of Tweets")

interact3 = pn.bind(create_plot, symbol=select3)

select4 = pn.widgets.Select(name='Select', options=symbols)


def post_img(symbol):
    x = "affordable_housing"
    str = f'https://github.com/ShawnP1337/AMS/blob/main/final_clouds/{symbol}_cloud.png?raw=true'
    return pn.pane.PNG(str, width=800, height=800)

interact4 = pn.bind(post_img, symbol=select4) 

#Dashboard Layout Usuing Template 

def build_dashboard():
    template = pn.template.FastListTemplate(
    title = "AMS Sentiment Analysis Dashboard",
    sidebar=[
        pn.pane.PNG('https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2F1000logos.net%2Fwp-content%2Fuploads%2F2017%2F06%2FTwitter-Logo.png&f=1&nofb=1&ipt=ab77e46cb8ae4d3d3cb5c0ead3fabbc762fb6cf708ba980603a49f9a34a30c1e&ipo=images', sizing_mode='scale_both'),
        pn.pane.Markdown("## Alex Wyatt, Mariane Modena, Shawn Pokharel"),
        pn.pane.Markdown("### Sentiment Analysis is the process of computationally identifying and categorizing opinions expressed in a piece of text, especially in order to determine whether the writer's attitude towards a particular topic, is positive, negative, or neutral."),
        pn.pane.Markdown("### We decided to perform Sentiment Analysis on Tweets. We wanted to know what the general population on Twitter thought of terms/topics related to the Housing Crisis."),
        pn.pane.Markdown("### Here is a dashboard of our results. The select dropdown menu can be used to switch between terms/topics"),
        pn.pane.Markdown("### NOTE: the '_' in-between a term should be assumed as a space. For instane 'cost_of_living' should be viewed as a 'cost of living' Twitter text query"),

    ],
    main = [pn.Row("### Positive sentiment: compound score >= 0.05 \n### Neutral sentiment: compound score > -0.05 and compound score < 0.05 \n### Negative sentiment: compound score <= -0.05 ",pn.Column(select1, interact)),
           pn.Row(pn.Column(select2,interact2)),
           pn.Row(pn.Column(select3,interact3)),
            pn.Row('# Word Clouds',pn.Column(select4,interact4))
           ]
           
           )
           
    return template


if __name__.startswith("bokeh"):
    # start with panel serve script.py
    dashboard = build_dashboard()
    dashboard.servable()
if __name__ == "__main__":
    # start with python script.py
    dashboard = build_dashboard()
    dashboard.show(port=5006)