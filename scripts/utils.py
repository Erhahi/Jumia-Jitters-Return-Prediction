# utils.py

import pandas as pd

def load_data(path):
    """Load CSV data from a given path."""
    return pd.read_csv(path)

def preprocess_data(df):
    """Apply optional preprocessing (placeholder)."""
    return df

def save_results(df, path):
    """Save DataFrame to a CSV file."""
    df.to_csv(path, index=False)
