import csv
import plotly.express as px
import numpy as np

def getdatasource(datapath):
    temp=[]
    icecreamsales=[]
    with open(datapath) as f:
        csvreader=csv.DictReader(f)
        for row in csvreader:
            temp.append(float(row["Temperature"]))
            icecreamsales.append(float(row["Ice-cream Sales"])) 

    return({"x":temp,"y":icecreamsales})

def findcorelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation i equal to : ", correlation)

def setup():
    datapath = "./icecream.csv"
    datasource = getdatasource(datapath)
    findcorelation(datasource)

setup()

