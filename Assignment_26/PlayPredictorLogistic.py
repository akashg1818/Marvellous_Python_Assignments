import pandas as pd
from sklearn.preprocessing import LabelEncoder 

def PlayPredictorLogistic(DataFrame):

    line = "-"*50

    df = pd.read_csv(DataFrame)

    print(line)
    print("Data loaded successfully")
    print(line)
    print(df.head())
    print(line)

    df.drop("Unnamed: 0", axis = 1,inplace = True)
    print("Updated dataset")
    print(line)
    print(df.head())
    print(line)

    df['Whether'] = df['Whether'].replace({'Sunny':0,'Overcast':1,'Rainy':2,})
    df['Temperature'] = df['Temperature'].replace({'Hot':0,'Mild':1,'Cool':2,})
    df['Play'] = df['Play'].replace({'No':0,'Yes':1})

    print("Data After Encoding")
    print(line)
    print(df.head())
    print(line) 

    print("Description about data ")
    print(line)
    print(df.describe())
    print(line)




def main():

    PlayPredictorLogistic("PlayPredictor.csv")


if __name__ == "__main__":
    main()