import pandas as pd

def Dataload():
    line = "-"*50

    data =[{'Name': 'Amit', 'Math' : 85, 'Science' : 92, 'English' : 75},{'Name': 'Sagar', 'Math' : 90, 'Science' : 88, 'English' : 85},{'Name': 'Pooja', 'Math' : 78, 'Science' : 80, 'English' : 82}]

    df = pd.DataFrame(data)

    print(line)
    print("Dataframe :")
    print(df)
    print(line)

    print("Data shape :",df.shape)
    print(line)
    print("Columns :",df.columns.tolist())
    print(line)
    print("Data types :")
    print(df.dtypes)
    print(line)
    print("Stastical information of data ")
    print(line)
    print(df.describe())
    

   
def main():

    Dataload()

if __name__ == "__main__":
    main()