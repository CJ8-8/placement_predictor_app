import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle
import os

os.makedirs("models", exist_ok=True)
df = pd.read_csv("data/synthetic_data.csv")

df["Tier"] = LabelEncoder().fit_transform(df["Tier"])
df["Placement"] = LabelEncoder().fit_transform(df["Placement"])

X = df.drop("Placement", axis=1)
y = df["Placement"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)
model = RandomForestClassifier(n_estimators=200, max_depth=10)
model.fit(X_train, y_train)

with open("models/placement_model.pkl", "wb") as f:
    pickle.dump(model, f)
