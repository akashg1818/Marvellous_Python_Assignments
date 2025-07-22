import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def Dataload():
    line = "-"*50

    data =[{'Name': 'Amit', 'Math' : 85, 'Science' : 92, 'English' : 75},{'Name': 'Sagar', 'Math' : 90, 'Science' : 88, 'English' : 85},{'Name': 'Pooja', 'Math' : 78, 'Science' : 80, 'English' : 82}]

    df = pd.DataFrame(data)

    print(df)
    df['Gender'] = ['Male','Male','Female']

    print(df)
    

    df_encoded = pd.get_dummies(df, columns=['Gender'])
    df_encoded[['Gender_Female', 'Gender_Male']] = df_encoded[['Gender_Female', 'Gender_Male']].astype(int)


    print(df_encoded)
   
 
def main():

    Dataload()

if __name__ == "__main__":
    main()