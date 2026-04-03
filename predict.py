import joblib
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def predict(input_data):
    try:
        # Load model
        model = joblib.load("model.pkl")

        # Convert input into DataFrame (FIXES WARNING)
        input_df = pd.DataFrame([[input_data]], columns=["area"])

        # Predict
        result = model.predict(input_df)

        return result[0]

    except Exception as e:
        logging.error(f"Error in prediction: {e}")
        return 0