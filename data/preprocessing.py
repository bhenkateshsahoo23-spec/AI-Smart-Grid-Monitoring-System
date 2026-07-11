"""
Data Preprocessing Module
AI Smart Grid Fault Detection Project
"""

import pandas as pd


def load_dataset(file_path):
    """
    Load the dataset from CSV.
    """
    df = pd.read_csv(file_path)
    return df


def show_dataset_info(df):
    """
    Display basic dataset information.
    """
    print("\n========== DATASET INFO ==========")
    print(df.info())

    print("\n========== FIRST 5 ROWS ==========")
    print(df.head())

    print("\n========== MISSING VALUES ==========")
    print(df.isnull().sum())

    print("\n========== STATISTICS ==========")
    print(df.describe())


if __name__ == "__main__":

    dataset = load_dataset("data/raw/smart_grid_dataset.csv")

    show_dataset_info(dataset)