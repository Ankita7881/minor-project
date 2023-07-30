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
st.title("DATASETS CONTENT")
def load_spend_data():
    df1 = pd.read_excel('datasets/car_data.xlsx',skiprows=2)
    df2 = pd.read_excel('datasets/car_data.xlsx',sheet_name=2,skiprows=0)
    df1.set_index('CAR ID', inplace=True)
    df2.set_index('CAR ID', inplace=True)
    df = df1.join(df2, how='left', rsuffix='_Customer')
    return df
with st.spinner("loading dataset"):
    df=load_spend_data()
st.sidebar.header("Navigation")

if st.sidebar.checkbox("Show Car's Datasets"):
    st.subheader('📅 Raw datasets')
    st.dataframe(df) 
    
st.subheader('Combined Analysis')
fig1 = px.area(df, 'Model Name ', 'On road Price ')
st.plotly_chart(fig1, use_container_width=True)

models = df['Model Name '].value_counts()
fig2 = px.pie(models, models.index, models.values)
st.plotly_chart(fig2, use_container_width=True)

