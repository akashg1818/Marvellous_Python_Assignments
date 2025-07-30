
import pandas as pd 

import matplotlib.pyplot as plt 
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression 

from sklearn.metrics import accuracy_score, classification_report

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
    #plt.show()

    sns.boxplot(x="Outcome", y = "BloodPressure",data = df)
    plt.title("Boxplot for Outcome by BloodPressure")
    #plt.show()

    sns.boxplot(x="Outcome", y = "Glucose",data = df)
    plt.title("Boxplot for Outcome by Glucose")
    #plt.show()

    df = df[df['BloodPressure']  != 0]
    df = df[df['Glucose']  != 0]
    print("Shape of data after removing values :",df.shape)
    print(line)

    X = df.drop(columns = ["Outcome"])
    Y = df["Outcome"]
    print("Shape of independent data :",X.shape)
    print("Shape of dependent data :",Y.shape)
    print(line)

    scaler = StandardScaler()
    X_Scaled = scaler.fit_transform(X)

    X_train,X_test,Y_train,Y_test = train_test_split(X_Scaled,Y, test_size = 0.2, random_state = 42)

    print("Sizes of splited data are :")
    print("Training Feature size :",X_train.shape)
    print("Training label size :",X_test.shape)
    print("Testing Feature size :",Y_train.shape)
    print("Testing Label size :",Y_test.shape)
    print(line)

    model = LogisticRegression()

    model.fit(X_train,Y_train)

    y_pred = model.predict(X_test)

    Accuracy = accuracy_score(y_pred,Y_test)

    print("Accuracy of model is :",Accuracy*100)
    

def main():

    DiabetesLogistic("diabetes.csv")


if __name__ == "__main__":
    main()