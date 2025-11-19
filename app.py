import streamlit as st   
import pandas as pd  
import plotly.express as px 
import numpy as np 


st.set_page_config(page_title="TESLA DASHBOARD", layout='wide')
st.title("Tesla Global Deliveries and Production Dashboard")
st.write("### From 2015 - 2025")

##cache load data

@st.cache_data
def load_data(path):
    df=pd.read_csv(path)
    return df  

df =load_data("Tesla2015-25.csv")
st.dataframe(df)