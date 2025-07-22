import pandas as pd
from sklearn.model_selection import train_test_split

def main():

    data = {
        'Age': [25, 30, 45, 35, 22],
        'Salary': [50000, 60000, 80000, 45000, 52000],
        'Purchased': [1, 0, 1, 0, 1]
    }
    df = pd.DataFrame(data)


    X = df[['Age', 'Salary']]        
    y = df['Purchased']              

if __name__ == "__main__":
    main()
