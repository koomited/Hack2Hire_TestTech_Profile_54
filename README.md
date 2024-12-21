[![TailwindCSS](https://img.shields.io/badge/Tailwind%20CSS-%2338B2AC.svg?logo=tailwind-css&logoColor=white)](#)
[![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?logo=visual-studio-code&logoColor=white)](#)
[![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black)](#)
[![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white)](#)
[![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=fff)](#)
![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)

![]( https://img.shields.io/badge/Use-white)
[![Trello](https://img.shields.io/badge/Trello-0052CC?logo=trello&logoColor=fff)](#)
![](https://img.shields.io/badge/with-yellow)
![](https://img.shields.io/badge/Vuejs-green)
![](https://img.shields.io/badge/and_-white)
![Laravel](https://img.shields.io/badge/laravel-%23FF2D20.svg?style=for-the-badge&logo=laravel&logoColor=white)
![](https://img.shields.io/badge/to-white)
![](https://img.shields.io/badge/build-white)
![VIBECAST](https://img.shields.io/badge/VIBECAST_-yellow)
![](https://img.shields.io/badge/at-black)
![](https://img.shields.io/badge/Epitech_Benin-blue)

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
   - Create dockerfile for api deployment.
   - Streamlit app : https://german-credit-analysis.streamlit.app/
   - Create dockerfile for streamlit app.
  

## Files Included

- `EDA.ipynb`: Jupyter notebook with analysis code.
- `eda_utils.py`: python file containing usefull functions for plots and some computations.
- `readme.md`: This file, providing an overview and instructions.
- `api.py`: api program using flask
- `Dockerfile`: dockerile for the api and streamlit app dockerization
- `test_api.py`: samal test of the api

## How to Use

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/Hack2Hire_TestTech_Profile_54.git
   cd Hack2Hire_TestTech_Profile_54
