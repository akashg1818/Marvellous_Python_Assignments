import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def Dataload():
    line = "-"*50

    data =[{'Name': 'Amit', 'Math' : 85, 'Science' : 92, 'English' : 75},{'Name': 'Sagar', 'Math' : 90, 'Science' : 88, 'English' : 85},{'Name': 'Pooja', 'Math' : 78, 'Science' : 80, 'English' : 82}]

    df = pd.DataFrame(data)

    print("Loaded data ")
    print(df)

    
    df['Gender'] = ['Male','Male','Female']

    print("Data after adding Gender column")
    print(df)

    grouped = df.groupby('Gender')[['Math', 'Science', 'English']].sum()

    print("Grouped data by gender with avg")

    print(grouped)

   
    
 
def main():

    Dataload()

if __name__ == "__main__":
    main()