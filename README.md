___
# Jumia-Jitters-Return-Prediction
A data science project for the DataVerse Africa Challenge that predicts product returns on Jumia, analyzes seller behavior, and provides actionable business recommendations using Python and machine learning.
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
├── pipeline/
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
