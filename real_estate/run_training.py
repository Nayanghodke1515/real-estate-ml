from data_preprocessing import load_data, clean_data
from train import train_model

# Load data
df = load_data()
df = clean_data(df)

# Features and target
X = df[["area"]]
y = df["price"]

# Train model
train_model(X, y)

print("Model training completed!")