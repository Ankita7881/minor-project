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
st.cache_data()
def load_customer_data():
    df = pd.read_excel('datasets/car_data.xlsx',sheet_name=2,skiprows=0)
    return df
with st.spinner("loading dataset"):
    df=load_customer_data()
st.sidebar.header("Navigation")

if st.sidebar.checkbox("Show Car's Datasets"):
    st.subheader('📅 Raw datasets')
    st.dataframe(df) 
    
total_sales=df['PRICE'].sum()
st.metric('Total Sales', f"Rs.{total_sales}",)

st.subheader('Comparison of models with the customer rating')
fig1 = px.bar(df, 'Customer Purchase Model Name ', 'Customer Satsfied Remarks  (1 to 10  number of rating)')
st.plotly_chart(fig1, use_container_width=True)


total_ass=df['Total Accessories Sale '].sum()
st.metric('Total Accessories Sales', f"Rs.{total_ass}",)

st.subheader('comparison of Customer Satsfied Remarks with CAR ID')
fig1 = px.bar(df, 'CAR ID', 'Customer Satsfied Remarks  (1 to 10  number of rating)')
st.plotly_chart(fig1, use_container_width=True)

st.subheader('comparison of Customer Purchase Model Name with Sales person Name ')
fig1 = px.bar(df, 'Customer Purchase Model Name ', 'Sales person Name ')
st.plotly_chart(fig1, use_container_width=True)

st.subheader('comparison of Customer name with Total Accessories Sale ')
fig1 = px.bar(df, 'Customer name ', 'Total Accessories Sale ')
st.plotly_chart(fig1, use_container_width=True)