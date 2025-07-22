import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics  

def Advertisement(Datapath):

    line = "-"*50
    df = pd.read_csv(Datapath)
    
    print(line)
    print("Dataset sample is ")
    print(line)
    print(df.head())

    print(line)
    print("Clean the dataset ")
    df.drop(columns = ['Unnamed: 0'], inplace = True)

    print("Updated datset is ")
    print(line)
    print(df.head())
    print(line) 

    print("Missing values in each column :")
    print(df.isnull().sum())
    print(line)

    print("Stastical summary :")
    print(line)
    print(df.describe())
    print(line)

    print("Correlation matrix")
    print(line)
    print(df.corr())
    print(line)


def main():

    Advertisement("Advertising.csv")


if __name__ == "__main__":
    main()

# AdvertisementRegression
