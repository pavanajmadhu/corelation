import csv
import plotly.express as px

with open("icecream.csv") as f:
    df=csv.DictReader(f)
    fig=px.scatter(df,x="Temperature",y="Ice-cream Sales")
    #to correctly plot y axis
    fig.update_layout(autotypenumbers="convert types")
    fig.show()

