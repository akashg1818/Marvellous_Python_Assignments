import pandas as pd 
import matplotlib.pyplot as plt 

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


    df = df[df['BloodPressure']  != 0]
    df = df[df['Glucose']  != 0]
    print("Shape of data after removing values :",df.shape)
    print(line) 

    



    

def main():

    DiabetesLogistic("diabetes.csv")


if __name__ == "__main__":
    main()