import os
import json
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import GridSearchCV, train_test_split
from joblib import dump
import sys
import pandas as pd

# Function to load data from CSV files in a given directory
def get_data(base_dir):
    data_file_names = [x for x in os.listdir(base_dir) if x.endswith('.csv')]
    data = {}
    for name in data_file_names:
        path_file = os.path.join(base_dir, name)
        data[name] = pd.read_csv("C:/Users/Shreshtha/PycharmProjects/pythonProject14/assets/data/iris.csv")
    return data

# Function to split data into training and testing sets
def split_data(data, test_size=0.2, random_state=42):
    df = data['iris.csv']
    X = df.drop('variety', axis=1)
    y = df['variety']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    return {'X_train': X_train, 'X_test': X_test, 'y_train': y_train, 'y_test': y_test}

# Function to train a logistic regression model
def train_model(X_train, y_train):
    clf = LogisticRegression(max_iter=1000, random_state=200)
    mod = GridSearchCV(clf, param_grid={'C': [0.001, 0.01, 0.1, 1, 10, 100]})
    mod.fit(X_train, y_train)
    m = mod.best_estimator_
    return m

# Function to save the trained model to a file
def save_model(m):
    dump(m, '../assets/model/logistic_regression.joblib')
    print("Model saved")

# Function to create classification metrics and save them to a JSON file
def create_metrics(X_test, y_test, clf):
    clf_report = classification_report(y_test, clf.predict(X_test))
    auc = roc_auc_score(y_test, clf.predict_proba(X_test)[:, 1])
    return {'auc': auc, 'clf_report': clf_report}

# Function to save metrics to a JSON file
def save_metrics(metrics):
    with open('../assets/model/logistic_regression_metrics.json', 'w') as out_file:
        json.dump(metrics, out_file, sort_keys=True, indent=4, ensure_ascii=False)

# Main script
if __name__ == "__main__":
    base_dir = r'C:\Users\Shreshtha\PycharmProjects\pythonProject14\assets\data'
    data = get_data(base_dir)

    split_data = split_data(data['iris.csv'])

    m = train_model(split_data['X_train'], split_data['y_train'])
    metrics = create_metrics(split_data['X_test'], split_data['y_test'], m)
    save_model(m)
    save_metrics(metrics)

