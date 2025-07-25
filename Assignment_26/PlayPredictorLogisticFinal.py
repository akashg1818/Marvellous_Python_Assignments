import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

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

    x = df[['Whether','Temperature']]
    y = df[['Play']]
    
    print("Shape of independent data :",x.shape)
    print("Shape of dependent data :",y.shape)
    print(line)

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2)

    print("Shape of x_train",x_train.shape)
    print("Shape of x_test",x_test.shape)
    print("Shape of y_train",y_train.shape)
    print("Shape of y_test",y_test.shape)
    print(line)

    model = LogisticRegression()

    model.fit(x_train,y_train)

    y_pred = model.predict(x_test)

    Accuracy = accuracy_score(y_pred,y_test)
    cm = confusion_matrix(y_test,y_pred)

    print("Accuracy of model is :",Accuracy*100,"%")
    print("Confusion matrix : ")
    print(cm)


    



    





def main():

    PlayPredictorLogistic("PlayPredictor.csv")


if __name__ == "__main__":
    main()