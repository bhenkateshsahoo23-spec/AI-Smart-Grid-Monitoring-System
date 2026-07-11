import pandas as pd
import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Number of samples
NUM_RECORDS = 10000

# Fault types
fault_types = [
    "Normal",
    "LG Fault",
    "LL Fault",
    "LLG Fault",
    "LLL Fault"
]

dataset = []

for _ in range(NUM_RECORDS):

    fault = random.choice(fault_types)

    if fault == "Normal":
        voltage = random.uniform(228, 232)
        current = random.uniform(5, 8)
        frequency = random.uniform(49.9, 50.1)
        pf = random.uniform(0.97, 1.00)
        temperature = random.uniform(25, 35)

    elif fault == "LG Fault":
        voltage = random.uniform(180, 220)
        current = random.uniform(10, 20)
        frequency = random.uniform(49.0, 49.8)
        pf = random.uniform(0.80, 0.95)
        temperature = random.uniform(35, 45)

    elif fault == "LL Fault":
        voltage = random.uniform(150, 200)
        current = random.uniform(15, 25)
        frequency = random.uniform(48.5, 49.5)
        pf = random.uniform(0.70, 0.90)
        temperature = random.uniform(40, 55)

    elif fault == "LLG Fault":
        voltage = random.uniform(100, 180)
        current = random.uniform(20, 35)
        frequency = random.uniform(47.5, 49.0)
        pf = random.uniform(0.60, 0.80)
        temperature = random.uniform(45, 65)

    else:   # LLL Fault
        voltage = random.uniform(80, 150)
        current = random.uniform(30, 45)
        frequency = random.uniform(47.0, 48.5)
        pf = random.uniform(0.50, 0.70)
        temperature = random.uniform(55, 75)

    power = (voltage * current * pf) / 1000

    dataset.append({
        "Timestamp": fake.date_time_this_year(),
        "Voltage(V)": round(voltage, 2),
        "Current(A)": round(current, 2),
        "Frequency(Hz)": round(frequency, 2),
        "Power(kW)": round(power, 2),
        "Power Factor": round(pf, 2),
        "Temperature(C)": round(temperature, 2),
        "Fault Type": fault
    })

df = pd.DataFrame(dataset)

# Save dataset
df.to_csv("data/raw/smart_grid_dataset.csv", index=False)

print("=" * 60)
print(" Smart Grid Dataset Generated Successfully")
print("=" * 60)
print(df.head())
print("\nTotal Records:", len(df))