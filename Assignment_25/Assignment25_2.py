import pandas as pd

def main():

    data = {'Name': ['A','B','C'], 'Age':[21.0,22.0,23.0] }

    df = pd.DataFrame(data)

    print(df)

    print("Before conversion:", df.dtypes)

    df['Age'] = df['Age'].astype(float)

    print("After conversion:", df.dtypes)

    print("Updated DataFrame:", df)


if __name__ == "__main__":
    main()