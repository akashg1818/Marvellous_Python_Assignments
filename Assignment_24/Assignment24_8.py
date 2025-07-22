import pandas as pd
import matplotlib.pyplot as plt

def Dataload():
    line = "-"*50

    data =[{'Name': 'Amit', 'Math' : 85, 'Science' : 92, 'English' : 75},{'Name': 'Sagar', 'Math' : 90, 'Science' : 88, 'English' : 85},{'Name': 'Pooja', 'Math' : 78, 'Science' : 80, 'English' : 82}]

    df = pd.DataFrame(data)

    print("Loaded data ")
    print(df)

    plt.figure(figsize=(6, 4))
    plt.hist(df['Math'], bins=5, color='skyblue', edgecolor='black')
    plt.title('Distribution of Math Marks')
    plt.xlabel('Math Marks')
    plt.ylabel('Number of Students')
    plt.grid(True)
    plt.show()

 
def main():

    Dataload()

if __name__ == "__main__":
    main()