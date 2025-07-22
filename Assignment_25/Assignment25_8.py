import pandas as pd
import numpy as np

def main():

    data = {'Marks': [45, 67, np.nan, 32, 76]}
    df = pd.DataFrame(data)

    df['Marks'] = df['Marks'].interpolate()

    print(df)

if __name__ == "__main__":
    main()
