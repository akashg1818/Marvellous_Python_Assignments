import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, RocCurveDisplay

def main():
    df=pd.read_csv("bank-full.csv",sep=";")
    print(df)

    print(df.shape)
    print(df.head())
    print(df.tail())
    print(df.info())
    print(df.describe()) 

    df=df.drop(columns=["duration"])
    print("after droping the duration column \n",df)

    
    #after mapping the y columns 
    df["y"] = df["y"].map({"yes": 1, "no": 0})
    print(df)


    # feature
    x=df.drop(columns=["y"])
    
    # label
    y=df["y"]

    print(x)
    print(y)




    # Split columns
    numeric_cols = x.select_dtypes(include=['int64',"float64"]).columns
    categorical_cols = x.select_dtypes(include=['object']).columns



   # Define preprocessing
    preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
       ]  
    )

    # divide data set in two parts for train and test purpose
    X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.2,random_state=42)


    models = {
    "Logistic Regression": LogisticRegression(max_iter=500),
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42)
    }

    for name, model in models.items():
       pipe = Pipeline([
        ('preprocess', preprocessor),
        ('classifier', model)
        ])
       


    pipe.fit(X_train, Y_train)   # this pipeline will train again and again as not saved in hardware darling it is on ram when script is running samjhya kya bhiduu
    y_pred = pipe.predict(X_test)
    y_proba = pipe.predict_proba(X_test)[:,1] # OK
    print(f"{name} Accuracy:", accuracy_score(Y_test, y_pred))


        # 5. Evaluation
    # ---------------------------
    print("\nConfusion Matrix:")
    cm = confusion_matrix(Y_test, y_pred)
    print(cm)

    # Plot heatmap for better visualization
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=["Predicted No", "Predicted Yes"],
                yticklabels=["Actual No", "Actual Yes"])
    plt.title("Confusion Matrix")
    plt.show()

    print("\n Classification Report:")
    print(classification_report(Y_test, y_pred))

    roc_score = roc_auc_score(Y_test, y_proba)
    print("\nROC-AUC Score:", roc_score)

    #Plot ROC Curve
    RocCurveDisplay.from_estimator(pipe, X_test, Y_test)
    plt.title("ROC Curve - Logistic Regression")
    plt.show()

   





if __name__=="__main__":
    main()    