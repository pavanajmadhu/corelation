import csv
import numpy as np

def getdatasource(datapath):
    size=[]
    timespent=[]
    with open(datapath) as f:
        csvreader=csv.DictReader(f)
        for row in csvreader:
            size.append(float(row["Size of TV"]))
            timespent.append(float(row["Average time "])) 

    return({"x":size,"y":timespent})

def findcorelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation i equal to : ", correlation)

def setup():
    datapath = "./sizeoftv.csv"
    datasource = getdatasource(datapath)
    findcorelation(datasource)

setup()

import csv
import plotly.express as px

with open("sizeoftv.csv") as f:
    df=csv.DictReader(f)
    fig=px.scatter(df,x="Size of TV",y="Average time ")
    fig.show()



