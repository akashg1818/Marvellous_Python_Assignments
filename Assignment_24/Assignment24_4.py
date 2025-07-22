import pandas as pd
import matplotlib.pyplot as plt

def Dataload():
    line = "-"*50

    data =[{'Name': 'Amit', 'Math' : 85, 'Science' : 92, 'English' : 75},{'Name': 'Sagar', 'Math' : 90, 'Science' : 88, 'English' : 85},{'Name': 'Pooja', 'Math' : 78, 'Science' : 80, 'English' : 82}]

    df = pd.DataFrame(data)

    print("Loaded data ")
    print(df)

    sagar_marks = df[df['Name'] == 'Sagar'][['Math', 'Science', 'English']].iloc[0]

    plt.figure(figsize=(6, 6))
    plt.pie(sagar_marks, labels=sagar_marks.index, autopct='%1.1f%%', startangle=90)
    plt.title("Sagar's Marks Distribution")
    plt.axis('equal')
    plt.show()

   
    
 
def main():

    Dataload()

if __name__ == "__main__":
    main()