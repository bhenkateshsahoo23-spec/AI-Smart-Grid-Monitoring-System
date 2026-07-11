import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/smart_grid_model.pkl")

# Load label encoder
encoder = joblib.load("models/label_encoder.pkl")


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