import pandas as pd 

import matplotlib.pyplot as plt 
import seaborn as sns

def DiabetesLogistic(Dataframe):

    line = "-"*100

    df = pd.read_csv(Dataframe)
    
    print(line)
    print("Dataset loaded successfully")
    print(line)
    print("First 5 entries of dataset are :")
    print(line)
    print(df.head())
    print(line)
    print("Statistical information about data:")
    print(line)
    print(df.describe())
    print(line)
    print(df.info())
    print(line) 

    plt.hist(df['Outcome'],color = 'skyblue',edgecolor = 'black')
    plt.xlabel("Outcome")
    plt.ylabel("Frequency")
    plt.title("Histogram for Diabities")
    plt.show()

    sns.boxplot(x="Outcome", y = "BloodPressure",data = df)
    plt.title("Boxplot for Outcome by BloodPressure")
    plt.show()

    sns.boxplot(x="Outcome", y = "Glucose",data = df)
    plt.title("Boxplot for Outcome by Glucose")
    plt.show()

    

def main():

    DiabetesLogistic("diabetes.csv")


if __name__ == "__main__":
    main()