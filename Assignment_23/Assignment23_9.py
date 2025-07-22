import pandas as pd
import matplotlib.pyplot as plt 

def Dataload():
    line = "-"*50

    data =[{'Name': 'Amit', 'Math' : np.nan, 'Science' : 92, 'English' : 75},{'Name': 'Sagar', 'Math' : 90, 'Science' : np.nan, 'English' : 85},{'Name': 'Pooja', 'Math' : 78, 'Science' : 80, 'English' : 82}]

    df = pd.DataFrame(data)

    print(line)
    print("Dataframe :")
    print(df)
    print(line)

    print("Data shape :",df.shape)
    print(line)
    
    

def main():

    Dataload()

if __name__ == "__main__":
    main()