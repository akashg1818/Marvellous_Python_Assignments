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
    
    HighScore = df[df['Science']>85]['Name']

    print("Students with more than 85 marks in Science :")
    print(HighScore.tolist())
    print(line)

    
def main():

    Dataload()

if __name__ == "__main__":
    main()