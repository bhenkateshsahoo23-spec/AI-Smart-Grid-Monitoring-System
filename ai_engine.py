import os
import joblib
import numpy as np
import pandas as pd

# ======================================================
# Load Model
# ======================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(
    os.path.join(BASE_DIR, "smart_grid_model.pkl")
)

label_encoder = joblib.load(
    os.path.join(BASE_DIR, "label_encoder.pkl")
)


# ======================================================
# Feature Names
# (Must exactly match the training dataset)
# ======================================================

FEATURE_COLUMNS = [
    "Voltage(V)",
    "Current(A)",
    "Frequency(Hz)",
    "Power(kW)",
    "Power Factor",
    "Temperature(C)"
]


# ======================================================
# Create DataFrame
# ======================================================

def prepare_features(voltage, current, frequency,
                     power, power_factor, temperature):

    return pd.DataFrame(
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


# ======================================================
# Live Prediction
# ======================================================

def predict_live_fault(live_data):

    features = prepare_features(
        live_data["voltage"],
        live_data["current"],
        live_data["frequency"],
        live_data["power"],
        live_data["power_factor"],
        live_data["temperature"]
    )

    prediction = model.predict(features)

    probability = model.predict_proba(features)

    confidence = round(
        float(np.max(probability) * 100),
        2
    )

    fault = label_encoder.inverse_transform(prediction)[0]

    return fault, confidence


# ======================================================
# Manual Prediction
# ======================================================

def predict_manual_fault(
    voltage,
    current,
    frequency,
    power,
    power_factor,
    temperature
):

    features = prepare_features(
        voltage,
        current,
        frequency,
        power,
        power_factor,
        temperature
    )

    prediction = model.predict(features)

    probability = model.predict_proba(features)

    confidence = round(
        float(np.max(probability) * 100),
        2
    )

    fault = label_encoder.inverse_transform(prediction)[0]

    return fault, confidence


# ======================================================
# Testing
# ======================================================

if __name__ == "__main__":

    sample = {
        "voltage": 230,
        "current": 5.2,
        "frequency": 50,
        "power": 1.20,
        "power_factor": 0.98,
        "temperature": 30
    }

    fault, confidence = predict_live_fault(sample)

    print("Predicted Fault :", fault)
    print("Confidence :", confidence, "%")
