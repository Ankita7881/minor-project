import streamlit as st 
import pandas as pd
import plotly.express as px
import numpy as np
# change plotly theme
#the set_page_config function is used to customize
#the configuration of your app's page. 
st.set_page_config(page_title="SALES PERFORMANCE DASHBOARD")

    # Your app code here...
st.title("Welcome to CAR'S SALES PERFORMANCE DASHBOARD ")
st.write("This is a sales performance dashboard app.")
#function to load the data only once
st.sidebar.title("DATASETS CONTENT")
st.cache_data()
def load_spend_data():
    df = pd.read_excel('datasets/car_data.xlsx',skiprows=2)
    return df
with st.spinner("loading dataset"):
    df=load_spend_data()
st.sidebar.header("Navigation")

if st.sidebar.checkbox("Show Car's Datasets"):
    st.subheader('📅 Raw datasets')
    st.dataframe(df) 

st.subheader('Car Details')
fig1 = px.bar(df, 'Brand Name ', 'Fuel Type ')
st.plotly_chart(fig1, use_container_width=True)
