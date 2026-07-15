import random

def get_live_data():

    voltage = round(random.uniform(218, 242), 2)
    current = round(random.uniform(4.5, 6.5), 2)
    frequency = round(random.uniform(49.8, 50.2), 2)
    power = round((voltage * current) / 1000, 2)
    power_factor = round(random.uniform(0.92, 0.99), 2)
    temperature = round(random.uniform(28, 36), 2)

    return {
        "voltage": voltage,
        "current": current,
        "frequency": frequency,
        "power": power,
        "power_factor": power_factor,
        "temperature": temperature
    }