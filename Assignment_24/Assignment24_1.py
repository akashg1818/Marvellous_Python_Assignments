import pandas as pd

def Dataload():
    line = "-"*50

    data =[{'Name': 'Amit', 'Math' : 85, 'Science' : 92, 'English' : 75},{'Name': 'Sagar', 'Math' : 90, 'Science' : 88, 'English' : 85},{'Name': 'Pooja', 'Math' : 78, 'Science' : 80, 'English' : 82}]

    df = pd.DataFrame(data)

    math_min = df['Math'].min()
    math_max = df['Math'].max()

    Normalized_math = (df['Math']- math_min)/(math_max - math_min)

    print(Normalized_math)
 
def main():

    Dataload()

if __name__ == "__main__":
    main()