import pandas as pd
from sklearn.neural_network import MLPRegressor
import joblib

def train_model():
    data = pd.read_csv("data.csv")
    
    X = data[["hours_study"]]
    y = data["exam_score"]
    
    model = MLPRegressor(hidden_layer_sizes=(10,), max_iter=1000)
    model.fit(X, y)
    
    joblib.dump(model, "model.pkl")

def predict(hours):
    model = joblib.load("model.pkl")
    result = model.predict([[hours]])
    return result[0]