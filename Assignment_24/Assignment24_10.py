import pandas as pd
import matplotlib.pyplot as plt

def Dataload():
    line = "-"*50

    data =[{'Name': 'Amit', 'Math' : 85, 'Science' : 92, 'English' : 75},{'Name': 'Sagar', 'Math' : 90, 'Science' : 88, 'English' : 85},{'Name': 'Pooja', 'Math' : 78, 'Science' : 80, 'English' : 82}]

    df = pd.DataFrame(data)

    print("Loaded data ")
    print(df)

    plt.figure(figsize=(5, 6))
    plt.boxplot(df['English'], patch_artist=True, boxprops=dict(facecolor='lightblue'))
    plt.title('Boxplot of English Marks')
    plt.ylabel('Marks')
    plt.grid(True)
    plt.show()


def main():

    Dataload()

if __name__ == "__main__":
    main()