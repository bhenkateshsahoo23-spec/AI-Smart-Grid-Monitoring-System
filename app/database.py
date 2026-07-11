import sqlite3


# -------------------------------------
# Create Database
# -------------------------------------

def create_database():

    connection = sqlite3.connect("smart_grid.db")

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS prediction_history (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        date TEXT,

        voltage REAL,

        current REAL,

        frequency REAL,

        power REAL,

        power_factor REAL,

        temperature REAL,

        fault TEXT,

        confidence REAL

    )
    """)

    connection.commit()
    connection.close()


# -------------------------------------
# Save Prediction
# -------------------------------------

def save_prediction(
    date,
    voltage,
    current,
    frequency,
    power,
    power_factor,
    temperature,
    fault,
    confidence
):

    connection = sqlite3.connect("smart_grid.db")

    cursor = connection.cursor()

    cursor.execute("""

    INSERT INTO prediction_history(

        date,
        voltage,
        current,
        frequency,
        power,
        power_factor,
        temperature,
        fault,
        confidence

    )

    VALUES(?,?,?,?,?,?,?,?,?)

    """,

    (
        date,
        voltage,
        current,
        frequency,
        power,
        power_factor,
        temperature,
        fault,
        confidence
    ))

    connection.commit()
    connection.close()


# -------------------------------------
# Get All Prediction History
# -------------------------------------

def get_prediction_history():

    connection = sqlite3.connect("smart_grid.db")

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM prediction_history ORDER BY id DESC"
    )

    data = cursor.fetchall()

    connection.close()

    return data


# -------------------------------------
# Delete All Prediction History
# -------------------------------------

def clear_history():

    connection = sqlite3.connect("smart_grid.db")

    cursor = connection.cursor()

    cursor.execute("DELETE FROM prediction_history")

    connection.commit()

    connection.close()