import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv("data/raw/smart_grid_dataset.csv")

print("\nDataset Loaded Successfully\n")


# -----------------------------
# Encode Target
# -----------------------------

encoder = LabelEncoder()

df["Fault Type"] = encoder.fit_transform(df["Fault Type"])


# -----------------------------
# Features
# -----------------------------

X = df[
    [
        "Voltage(V)",
        "Current(A)",
        "Frequency(Hz)",
        "Power(kW)",
        "Power Factor",
        "Temperature(C)"
    ]
]

y = df["Fault Type"]


# -----------------------------
# Train Test Split
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# -----------------------------
# Train Model
# -----------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("Model Trained Successfully")


# -----------------------------
# Prediction
# -----------------------------

prediction = model.predict(X_test)


# -----------------------------
# Accuracy
# -----------------------------

accuracy = accuracy_score(y_test, prediction)

print("\nAccuracy : ", accuracy)


print("\nClassification Report\n")

print(classification_report(y_test, prediction))


print("\nConfusion Matrix\n")

print(confusion_matrix(y_test, prediction))


# -----------------------------
# Save Model
# -----------------------------

joblib.dump(model, "models/smart_grid_model.pkl")

joblib.dump(encoder, "models/label_encoder.pkl")


print("\nModel Saved Successfully")