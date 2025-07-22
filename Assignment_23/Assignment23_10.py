import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

def main():

    data = data =[{'Name': 'Amit', 'Math' : 85, 'Science' : 92, 'English' : 75},
    {'Name': 'Sagar', 'Math' : 90, 'Science' : 88, 'English' : 85},
    {'Name': 'Pooja', 'Math' : 78, 'Science' : 80, 'English' : 82}]

    df = pd.DataFrame(data)

    print(df)

    df_new = df.drop(columns = ['English'])

    print(df)


if __name__ == "__main__":
    main()