from django.shortcuts import render
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd
import os

# Load and preprocess data once
def load_data():
    dataframe = pd.read_csv(r"C:\Users\malik\Documents\machine\myenv\placement-dataset.csv")
    dataframe['Gender'].replace({'Male': 0, 'Female': 1}, inplace=True)
    dataframe['Stream'].replace(
        {'Electronics And Communication': 0, 'Computer Science': 1, 'Information Technology': 2,
         'Mechanical': 3, 'Electrical': 4, 'Civil': 5}, inplace=True)
    return dataframe

dataframe = load_data()
Y = dataframe["PlacedOrNot"]
X = dataframe.drop(["PlacedOrNot"], axis=1)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1)
model = LogisticRegression()
model.fit(X_train, Y_train)

def index(request):
    return render(request, "index.html")

def predict(request):
    return render(request, "predict.html")

def result(request):
    try:
        val1 = float(request.GET.get('n1', 0))
        val2 = float(request.GET.get('n2', 0))
        val3 = float(request.GET.get('n3', 0))
        val4 = float(request.GET.get('n4', 0))
        val5 = float(request.GET.get('n5', 0))
        val6 = float(request.GET.get('n6', 0))
        val7 = float(request.GET.get('n7', 0))

        pred = model.predict([[val1, val2, val3, val4, val5, val6, val7]])

        result1 = "You are placed!" if pred == [1] else "You are not placed!"
    except Exception as e:
        result1 = f"Error: {str(e)}"

    return render(request, "predict.html", {"result2": result1})