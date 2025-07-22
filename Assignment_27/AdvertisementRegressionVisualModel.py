import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics  

def Advertisement(Datapath):

    line = "-"*50
    df = pd.read_csv(Datapath)
    
    print(line)
    print("Dataset sample is ")
    print(line)
    print(df.head())

    print(line)
    print("Clean the dataset ")
    df.drop(columns = ['Unnamed: 0'], inplace = True)

    print("Updated datset is ")
    print(line)
    print(df.head())
    print(line) 

    print("Missing values in each column :")
    print(df.isnull().sum())
    print(line)

    print("Stastical summary :")
    print(line)
    print(df.describe())
    print(line)

    print("Correlation matrix")
    print(line)
    print(df.corr())
    print(line)

    plt.figure(figsize =(12,8))
    sns.heatmap(df.corr(),annot = True, cmap = 'coolwarm')
    plt.title("Correlation Heatmap")
    plt.show()

    sns.pairplot(df)
    plt.suptitle("Pairplot of Features ",y = 1.02)
    plt.show()

    x = df[['TV','radio','newspaper']]
    y = df['sales']

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2, random_state = 42)

    model = LinearRegression()
    model.fit(x_train,y_train)

    y_pred = model.predict(x_test)

    MSE = metrics.mean_squared_error(y_pred,y_test)
    RMSE = np.sqrt(MSE)
    r2 = metrics.r2_score(y_pred,y_test)
    
    print(line)
    print("Mean squared error is :",MSE)
    print("Root mean squared error is :",RMSE)
    print("r2 value is :",r2)
    print(line)

    print("Model coefficient are :")
    print(line)
    for col, coef in zip(x.columns, model.coef_):
        print(f"{col} : {coef}") 
    
    print("Y Intercept is ",model.ntercept_)

    plt.figure(figsize =(12,8))
    plt.scatter(y_test,y_pred,color = 'blue')
    plt.xlabel('Acutal sales')
    plt.ylabel('Predicted sales ')
    plt.title("Advertisement")
    plt.grid(True)
    plt.show()



def main():

    Advertisement("Advertising.csv")


if __name__ == "__main__":
    main()

# AdvertisementRegression
