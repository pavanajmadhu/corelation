import csv
import numpy as np

def getdatasource(datapath):
    marks=[]
    attendance=[]
    with open(datapath) as f:
        csvreader=csv.DictReader(f)
        for row in csvreader:
            marks.append(float(row["Marks In Percentage"]))
            attendance.append(float(row["Days Present"])) 

    return({"x":marks,"y":attendance})

def findcorelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation i equal to : ", correlation)

def setup():
    datapath = "./students.csv"
    datasource = getdatasource(datapath)
    findcorelation(datasource)

setup()

import csv
import plotly.express as px

with open("students.csv") as f:
    df=csv.DictReader(f)
    fig=px.scatter(df,x="Marks In Percentage",y="Days Present")
    fig.update_yaxes(rangemode="tozero")
    fig.show()



