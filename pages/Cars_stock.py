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
def load_data():
    df = pd.read_excel('datasets/car_data.xlsx',sheet_name=1,skiprows=2)
    return df
with st.spinner("loading dataset"):
    df=load_data()
st.sidebar.header("Navigation")

if st.sidebar.checkbox("Show Car's Datasets"):
    st.subheader('📅 Raw datasets')
    st.dataframe(df) 


st.subheader('Cars_stock')
fig1 = px.bar(df, 'Wholesale Vehicle Model Name ', 'Total Vehicle Retail ')
st.plotly_chart(fig1, use_container_width=True)

st.subheader('datacount of month')
models = df['Month '].value_counts()
fig2 = px.funnel(models, models.index, models.values)
st.plotly_chart(fig2, use_container_width=True)

total_vehicle=df['Total Vehicle Retail '].sum()
st.metric('Total Number of Vehicles Retail:', f"{total_vehicle}",)

st.subheader('No.of vehicles retail in a month')

result_df =df.groupby('Month ')['Total Vehicle Wholesale '].sum().reset_index()
fig1 = px.bar(result_df, 'Month ','Total Vehicle Wholesale ')
st.plotly_chart(fig1, use_container_width=True)