import joblib

def predict(data):
    model = joblib.load("model.pkl")
    result = model.predict([data])
    return result[0]