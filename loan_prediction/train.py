import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# Load data
data = pd.read_csv("data.csv")

# Features and target
X = data[["income", "loan_amount", "credit_score"]]
y = data["approved"]

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("Model trained and saved!")