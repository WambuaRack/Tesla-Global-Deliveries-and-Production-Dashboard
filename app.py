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

##sidebar filters

st.sidebar.header("Filter Application")
region =["ALL"]+sorted(df['Region'].dropna().unique().tolist())
selected_region=st.sidebar.selectbox("Region", region)

Year =["ALL"]+sorted(df['Year'].dropna().unique().tolist())
selected_year=st.sidebar.selectbox("Year", Year)

Model =["ALL"]+sorted(df['Model'].dropna().unique().tolist())
selected_Model=st.sidebar.selectbox("Model", Model)

Month =["ALL"]+sorted(df['Month'].dropna().unique().tolist())
selected_Month=st.sidebar.selectbox("Month", Month)

Source_Type =["ALL"]+sorted(df['Source_Type'].dropna().unique().tolist())
selected_Source_Type=st.sidebar.selectbox("Source Type", Source_Type)

min_km, max_km =int(df["Range_km"].min()), int(df["Range_km"].max())
KM_range =st.sidebar.slider("Kilometre Range", min_km,max_km,(min_km,max_km))

##applying filters
filtered =df.copy()
if selected_Model !="ALL":
    filtered=filtered[filtered["Model"]== selected_Model]
if selected_region !="ALL":
    filtered=filtered[filtered["Region"]== selected_region]  

if selected_Source_Type !="ALL":
    filtered=filtered[filtered["Source_Type"]== selected_Source_Type]  
    
if selected_Month !="ALL":
    filtered=filtered[filtered["Month"]== selected_Month]  
    
if selected_year !="ALL":
    filtered=filtered[filtered["Year"]== selected_year]  


filtered=filtered[(filtered['Range_km']>=KM_range[0]) & (filtered['Range_km']<=KM_range[1])]
    