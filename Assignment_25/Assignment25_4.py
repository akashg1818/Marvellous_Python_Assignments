import pandas as pd

def main():

    data = {'Department': ['HR', 'IT', 'Finance', 'HR', 'IT']}
    df = pd.DataFrame(data)


    df_encoded = pd.get_dummies(df, columns=['Department'])

    print(df_encoded)

if __name__ == "__main__":
    main()
