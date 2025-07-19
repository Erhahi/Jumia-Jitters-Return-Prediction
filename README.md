___
# Dataverse Africa Challenge – E-Commerce Returns & Seller Profiling

## Overview
This project analyzes real-world e-commerce data from Jumia to uncover return risk patterns and seller behaviors. It combines data analysis, predictive modeling, and business recommendations to help reduce logistics costs and identify risky sellers.
___
## Phases Completed
1. **Data Exploration** – Explored 987 records from the Jumia dataset (`jumia_jitters_dataset.csv`)
2. **Market Insights** – Analyzed product prices, delays, customer reviews, and seller activity
3. **Modeling Return Risk** – Built logistic regression to predict return likelihood (AUC: 0.91)
4. **Strategic Recommendations** – Proposed actionable insights for seller risk monitoring
5. **Script Pipeline** – Packaged reusable Python scripts for scalable deployment

## Key Insights
- **Late delivery** and **low customer ratings** drive return risk
- Certain sellers have unusually high return rates
- Sentiment analysis of customer reviews adds strong predictive power

## Files & Structure

___
```
jumia-jitters-return-prediction/
├── data/
│   └── jumia_jitters_dataset.csv           # Raw dataset
├── cleaned/
│   ├── cleaned_orders.csv                  # Cleaned dataset
│   └── seller_summary.csv                  
│   └── seller_risk_action.csv
│   └── risky_sellers.csv
│   └── orders_with_return_risk.csv
│   └── model_performance_metrics.csv
│ 
├── models/
│   └── return_prediction_model.pkl         # Saved model
│   └── scaler.pkl                          # Scaler object
│                      
├── scripts/
│   ├── config.py                           # Config variables
│   ├── utils.py                            # Feature engineering & preprocessing
│   └── run_pipeline.py                     # Script to run predictions
│
├── charts/
│   ├── top_states_bar_chart.png
│   ├── avg_rating_by_state.png
│   ├── top_returning_sellers.png
│   ├── roc_curve_plot.png
│   └── feature_importance.png
│
├── notebooks/
│   └── Phase_1_Data_Cleaning_Feature_Engineering_Erhahi_Deborah.ipynb
│   └── Phase_2_Analytics_Visuals_Erhahi_Deborah.ipynb
│   └── Phase_3_Modeling_Return_Risk_Erhahi_Deborah.ipynb
│   └── Phase_4_Strategic_Recommendations_Erhahi_Deborah.ipynb    
│ 
├── outputs/
│   └── return_predictions.csv
│   
└──  charts/                      
```

## Run the Pipeline
```bash
# Navigate to the scripts folder and run:
python run_pipeline.py
```
