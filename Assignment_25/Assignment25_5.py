import pandas as pd
from sklearn.model_selection import train_test_split


def main():

    data = {'Age': [22, 25, 47, 52, 46, 56],'Purchased': [0, 1, 1, 0, 1, 0]}


    df = pd.DataFrame(data)

    X = df[['Age']]        
    y = df['Purchased'] 

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


    print("X_train:", X_train)
    print("X_test:", X_test)
    print("y_train:", y_train)
    print("y_test:", y_test)

if __name__ == "__main__":
    main()
