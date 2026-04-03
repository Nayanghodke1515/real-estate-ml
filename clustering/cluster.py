import pandas as pd
from sklearn.cluster import KMeans

def get_clusters():
    data = pd.read_csv("data.csv")
    
    model = KMeans(n_clusters=2, random_state=42)
    data["cluster"] = model.fit_predict(data[["age", "income"]])
    
    return data