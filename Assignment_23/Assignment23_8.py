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

    df = df.drop('TotalMarks',axis=1)
    print(df)
    print(line)

    amit_data = df[df['Name'] == 'Amit'][['Math', 'Science', 'English']].iloc[0]

    plt.figure(figsize=(8, 5))
    plt.plot(amit_data.index, amit_data.values, marker='o', color='red')

    plt.title("Amit's Marks Across Subjects")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.grid(True)
    plt.show()

def main():

    Dataload()

if __name__ == "__main__":
    main()