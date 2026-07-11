import os
import joblib
import pandas as pd

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load model and encoder
model = joblib.load(
    os.path.join(BASE_DIR, "smart_grid_model.pkl")
)

encoder = joblib.load(
    os.path.join(BASE_DIR, "label_encoder.pkl")
)


def predict_fault(voltage, current, frequency, power, power_factor, temperature):

    values = pd.DataFrame({
        "Voltage(V)": [voltage],
        "Current(A)": [current],
        "Frequency(Hz)": [frequency],
        "Power(kW)": [power],
        "Power Factor": [power_factor],
        "Temperature(C)": [temperature]
    })

    prediction = model.predict(values)
    probability = model.predict_proba(values)

    confidence = probability.max() * 100

    fault = encoder.inverse_transform(prediction)[0]

    return fault, confidence
