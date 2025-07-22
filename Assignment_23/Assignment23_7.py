import pandas as pd
import matplotlib.pyplot as plt 

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
    
    df['TotalMarks'] = df[['Math','Science','English']].sum(axis =1)

    print("Updated dataframe is :")
    print(line)
    print(df)
    print(line)

    plt.bar(df['Name'],df['TotalMarks'])
    plt.title("Bar Plot")
    plt.xlabel("Name of Student")
    plt.ylabel("Total Marks")
    plt.show()

    
   
def main():

    Dataload()

if __name__ == "__main__":
    main()