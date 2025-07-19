# run_pipeline.py

import pandas as pd
import joblib
from config import CLEANED_DATA_PATH, MODEL_PATH, SCALER_PATH, PREDICTIONS_OUTPUT_PATH
from utils import load_data, preprocess_data, save_results

def main():
    # Load the cleaned dataset
    df = load_data(CLEANED_DATA_PATH)
    df = preprocess_data(df)

    # Define the features used during training
    features = [
        'price', 'quantity', 'order_value', 'delivery_delay', 
        'is_late', 'customer_rating', 'sentiment_score', 
        'has_complaint', 'low_rating'
    ]
    X = df[features]

    # Load the model and scaler
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

    # Scale the features
    X_scaled = scaler.transform(X)

    # Predict return risk
    df['return_probability'] = model.predict_proba(X_scaled)[:, 1]
    df['return_prediction'] = model.predict(X_scaled)

    # Save results
    save_results(df, PREDICTIONS_OUTPUT_PATH)
    print(" Return predictions saved to:", PREDICTIONS_OUTPUT_PATH)

if __name__ == "__main__":
    main()
    print(" Pipeline executed successfully.")
