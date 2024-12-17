import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import pickle
import numpy as np

st.markdown(
    "<h2 style='text-align: center;'>Model Predictions</h2>", 
    unsafe_allow_html=True
)

# Import model
with open('../best_rf.pkl', 'rb') as f:
    model = pickle.load(f)
    
# entry form

with st.form("my_form"):
    
    Age = st.slider("Age", 0, 100)
    Credit_amount= st.number_input("Credit amount")
    Purpose= st.number_input('Credit Purpose', min_value=0, max_value=7, value=5, step=1)
    Duration= st.number_input('Credit Duration (months)', min_value=0)
    
    submitted = st.form_submit_button("Submit")
    
if submitted:
        
    model_data = np.array([ Credit_amount, Age, Duration, Purpose]).reshape(1,-1)
    prediction_prob = model.predict_proba(model_data)[:,1]
    
    
    with st.container():
        if prediction_prob[0] < 0.5:
            # Green Box for Approved
            st.markdown(
                f"""
                <div style="
                    border: 2px solid green; 
                    padding: 16px; 
                    border-radius: 10px; 
                    width: 50%; 
                    margin: auto; 
                    text-align: center;">
                    <h3 style="color: green;">Bad Credit Score: {round(prediction_prob[0], 4)}</h3>
                    <h3 style="color: green;">Decision: Credit Approved</h3>
                </div>
                """, unsafe_allow_html=True
            )
        else:
            # Red Box for Rejected
            st.markdown(
                f"""
                <div style="
                    border: 2px solid red; 
                    padding: 16px; 
                    border-radius: 10px; 
                    width: 50%; 
                    margin: auto; 
                    text-align: center;">
                    <h3 style="color: red;">Bad Credit Score: {round(prediction_prob[0], 4)}</h3>
                    <h3 style="color: red;">Decision: Credit Rejected</h3>
                </div>
                """, unsafe_allow_html=True
            )
        

    