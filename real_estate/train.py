from sklearn.linear_model import LinearRegression
import joblib
import logging

logging.basicConfig(level=logging.INFO)

def train_model(X, y):
    try:
        model = LinearRegression()
        model.fit(X, y)
        joblib.dump(model, "model.pkl")
        logging.info("Model trained and saved successfully")
        return model
    except Exception as e:
        logging.error(f"Error in training: {e}")