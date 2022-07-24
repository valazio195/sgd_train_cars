#ISENG DOANG

import pandas as pd
import pickle 

from helper.data_check_preparation import *
from helper.feature_eng import feature_eng
from helper.constant import PATH, INIT_COLUMN
from helper.models import SGDClass
from helper.preprocess import standard_scaler

from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, precision_score, recall_score, f1_score

def train_model():
    # pembacaan dan pengecekan data
    cars_data = read_and_change(PATH)
    
    # feature engineering
    df_transformed = feature_engineering(cars_data)
    print("Start Saving Result Feature Engineering!")
    df_transformed.to_csv("artifacts/df_transformed.csv")
    
    # siapkan fitur data dan target data 
    X = df_transformed.drop(columns=['price'])
    y = df_transformed["price"]
    
    # data splitting
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)
    
    # scaler
    train_scaler, X_train_scaled = standard_scaler(X_train)
    pickle.dump(train_scaler, open("artifacts/train_scaler.pkl", "wb"))
    X_test_scaled = train_scaler.transform(X_test)
    
    print("Start Saving Result Standard Scaler!")
    X_train_scaled.to_csv("artifacts/X_train_scaled.csv")
    
    # define model and start training
    clf_model = SGDClass["sgdclass"]
    clf_model.fit(X_train_scaled, y_train)
    y_pred_class = clf_model.predict_proba(X_test_scaled).argmax(1)
    y_pred_proba = clf_model.predict_proba(X_test_scaled)[:, 1]

    pickle.dump(clf_model, open("artifacts/logreg_model.pkl", "wb"))
    
    # show training result
    print("------------------------------")
    print("Model Performance:")
    print("ROC_AUC:", roc_auc_score(y_test, y_pred_proba))
    print("Recall:", recall_score(y_test, y_pred_class))
    print("Precision:", precision_score(y_test, y_pred_class))
    print("f1_score:", f1_score(y_test, y_pred_class, average="macro")) 
    
if __name__ == "__main__":
    print("START RUNNING PIPELINE!")
    train_model()
    print("FINISH RUNNING PIPELINE!")