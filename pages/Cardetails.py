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

st.subheader('VALUE COUNT OF MODEL NAME')
models = df['Model Name '].value_counts()
fig2 = px.funnel(models, models.index, models.values)
st.plotly_chart(fig2, use_container_width=True)

st.subheader('ANALYSIS ON PRICE AND MODEL NAME')
fig1 = px.area(df, 'Model Name ', 'On road Price ')
st.plotly_chart(fig1, use_container_width=True)

st.subheader('ANALYSIS ON PRICE AND MODEL NAME')
fig2 = px.bar(df, 'CAR ID',['On road Price ','Ex Showroom Price '],hover_name='Model Name ', barmode='group')
st.plotly_chart(fig2, use_container_width=True)

st.subheader('Analysis on fuel type vehicle')
vehicle_fuel=df['Fuel Type '].value_counts()
chart1 = px.pie(vehicle_fuel,vehicle_fuel.index,vehicle_fuel.values)
st.plotly_chart(chart1, use_container_width=True)
