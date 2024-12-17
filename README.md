# German Credit Dataset Analysis

## Overview

This project analyzes the German Credit Dataset to cluster customers and classify loan applicants as either Good or Bad credit risks. The dataset comprises 1000 entries with various attributes, and the goal is to develop a credit scoring prediction model, deploy it using Docker, and create an interactive dashboard Power BI to visualize the results..

## Tasks Performed

1. **Exploratory Data Analysis (EDA) and Data Cleaning:**
   - Investigated the dataset for missing values and anomalies.
   - Removed irrelevant columns with obscure descriptions.

2. **One-Hot Encoding:**
   - Applied one-hot encoding for categorical variables.

3. **Histogram Visualization:**
   - Visualized histograms of numerical features.
   - Applied log transformation to normalize data.

4. **Feature Scaling:**
   - Ensured consistent scaling of numerical features.

5. **Modeling and Evaluation:**
   - Implemented K-Fold Cross-Validation with Random Forest.
   - Reported evaluation metrics.
  
6. **Deployment:**
   - Create api with flask.
   - Create dockerfile for model deployment.

   - Streamlit app: https://german-credit-analysis.streamlit.app/

## Files Included

- `EDA.ipynb`: Jupyter notebook with analysis code.
- `utils.py`: python file containing usefull functions for plots and some computations.
- `readme.md`: This file, providing an overview and instructions.
- `api.py`: api program using flask
- `Dockerfile`: dockerile for the model dockerization
- `test_request.py`: samal test of the api

## How to Use

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/Hack2Hire_TestTech_Profile_54.git
   cd Hack2Hire_TestTech_Profile_54
