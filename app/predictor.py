import os
import joblib
import pandas as pd
import numpy as np

# ======================================
# Load AI Model
# ======================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)
MODEL_DIR = os.path.join(PROJECT_DIR, "models")

model = joblib.load(
    os.path.join(MODEL_DIR, "smart_grid_model.pkl")
)

encoder = joblib.load(
    os.path.join(MODEL_DIR, "label_encoder.pkl")
)

# ======================================
# Feature Names
# ======================================

FEATURE_COLUMNS = [
    "Voltage(V)",
    "Current(A)",
    "Frequency(Hz)",
    "Power(kW)",
    "Power Factor",
    "Temperature(C)"
]

# ======================================
# Prediction Function
# ======================================

def predict_fault(voltage,
                  current,
                  frequency,
                  power,
                  power_factor,
                  temperature):

    values = pd.DataFrame(
        [[
            voltage,
            current,
            frequency,
            power,
            power_factor,
            temperature
        ]],
        columns=FEATURE_COLUMNS
    )

    prediction = model.predict(values)

    probability = model.predict_proba(values)

    confidence = round(
        float(np.max(probability) * 100),
        2
    )

    fault = encoder.inverse_transform(prediction)[0]

    return fault, confidence


# ======================================
# Testing
# ======================================

if __name__ == "__main__":

    fault, confidence = predict_fault(
        230,
        5.5,
        50,
        1.2,
        0.98,
        30
    )

    print("Fault :", fault)
    print("Confidence :", confidence, "%")