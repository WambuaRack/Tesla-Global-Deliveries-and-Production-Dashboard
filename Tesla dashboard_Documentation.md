### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 10:26:18 AM*

**[REMOVED]**
```
(from line ~104)
    fig1=px.bar(price_year,x='Region', y='Avg_Price_USD', color="Region", title="Total Price Per Region")
    st.plotly_chart(fig1, use_container_width=True)
```
**[ADDED]**
```
104       fig3=px.bar(price_region,x='Region', y='Avg_Price_USD', color="Region", title="Total Price Per Region")
105       st.plotly_chart(fig3, use_container_width=True)
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 10:25:21 AM*

**[REMOVED]**
```
(from line ~104)
    fig1=px.bar(price_year,x='Region', y='Avg_Price_USD', title="Total Price Per Year")
    fig1.update_traces(line=dict(color ='yellow', width =3))

```
**[ADDED]**
```
104       fig1=px.bar(price_year,x='Region', y='Avg_Price_USD', color="Region", title="Total Price Per Region")
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 10:24:48 AM*

**[REMOVED]**
```
(from line ~104)
    fig1=px.bar(price_year,x='Region', y='Avg_Price_USD', markers=True,title="Total Price Per Year")

```
**[ADDED]**
```
104       fig1=px.bar(price_year,x='Region', y='Avg_Price_USD', title="Total Price Per Year")
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 10:24:16 AM*

**[REMOVED]**
```
(from line ~103)
    price_year =filtered.groupby('Region')['Avg_Price_USD'].sum().reset_index()
    fig1=px.line(price_year,x='Region', y='Avg_Price_USD', markers=True,title="Total Price Per Year")

```
**[ADDED]**
```
103       price_region =filtered.groupby('Region')['Avg_Price_USD'].sum().reset_index()
104       fig1=px.bar(price_year,x='Region', y='Avg_Price_USD', markers=True,title="Total Price Per Year")
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 10:24:00 AM*

**[ADDED]**
```
100       st.plotly_chart(fig1, use_container_width=True)
101       
102   with c1:
103       price_year =filtered.groupby('Region')['Avg_Price_USD'].sum().reset_index()
104       fig1=px.line(price_year,x='Region', y='Avg_Price_USD', markers=True,title="Total Price Per Year")
105       fig1.update_traces(line=dict(color ='yellow', width =3))
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 10:22:39 AM*

**[REMOVED]**
```
(from line ~94)
    fig1.update_traces(line=dict(color ='blue', width =3))

```
**[ADDED]**
```
94        fig1.update_traces(line=dict(color ='yellow', width =3))
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 10:22:16 AM*

**[REMOVED]**
```
(from line ~96)
with c1:

```
**[ADDED]**
```
96    with c2:
```
**[REMOVED]**
```
(from line ~99)
    fig1.update_traces(line=dict(color ='blue', width =3))

```
**[ADDED]**
```
99        fig1.update_traces(line=dict(color ='red', width =3))
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 10:21:47 AM*

**[REMOVED]**
```
(from line ~97)
    prod_units =filtered.groupby('Year')['Avg_Price_USD'].sum().reset_index()
    fig1=px.line(price_year,x='Year', y='Avg_Price_USD', markers=True,title="Total Price Per Year")

```
**[ADDED]**
```
97        prod_units =filtered.groupby('Year')['Production_Units'].sum().reset_index()
98        fig1=px.line(prod_units,x='Year', y='Production_Units', markers=True,title="Total Price Per Year")
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 10:21:29 AM*

**[ADDED]**
```
95        st.plotly_chart(fig1, use_container_width=True)
96    with c1:
97        prod_units =filtered.groupby('Year')['Avg_Price_USD'].sum().reset_index()
98        fig1=px.line(price_year,x='Year', y='Avg_Price_USD', markers=True,title="Total Price Per Year")
99        fig1.update_traces(line=dict(color ='blue', width =3))
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 10:19:30 AM*

**[REMOVED]**
```
(from line ~88)
    )
```
**[ADDED]**
```
88        )
89        
90    c1, c2 =st.columns(2)
91    with c1:
92        price_year =filtered.groupby('Year')['Avg_Price_USD'].sum().reset_index()
93        fig1=px.line(price_year,x='Year', y='Avg_Price_USD', markers=True,title="Total Price Per Year")
94        fig1.update_traces(line=dict(color ='blue', width =3))
95        st.plotly_chart(fig1, use_container_width=True)
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 10:13:58 AM*

**[REMOVED]**
```
(from line ~87)
        

```
**[ADDED]**
```
87            delta="Top Region listing"
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 10:13:19 AM*

**[REMOVED]**
```
(from line ~69)
lat_region = filtered["Region"].value_counts().idxmin()

```
**[REMOVED]**
```
(from line ~87)
        delta=f"Bottom Region {lat_region}"

```
**[ADDED]**
```
87            
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 10:12:55 AM*

**[REMOVED]**
```
(from line ~88)
        delta=f"Region {top_models}"

```
**[ADDED]**
```
88            delta=f"Bottom Region {lat_region}"
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 10:12:29 AM*

**[REMOVED]**
```
(from line ~68)
top_models = filtered["Model"].value_counts().nlargest(1)

```
**[ADDED]**
```
69    lat_region = filtered["Region"].value_counts().idxmin()
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 10:11:09 AM*

**[REMOVED]**
```
(from line ~86)
        label="Top Models",
        value=f"{top_models}",
        delta=f"Region {top_region}"

```
**[ADDED]**
```
86            label="Top Region",
87            value=f"{top_region}",
88            delta=f"Region {top_models}"
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 10:09:59 AM*

**[REMOVED]**
```
(from line ~68)
top_models = filtered["Model"].value_counts().nlargest()

```
**[ADDED]**
```
68    top_models = filtered["Model"].value_counts().nlargest(1)
```
**[REMOVED]**
```
(from line ~87)
        value={top_models},

```
**[ADDED]**
```
87            value=f"{top_models}",
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 10:09:31 AM*

**[REMOVED]**
```
(from line ~87)
        value=f"{top_models}",

```
**[ADDED]**
```
87            value={top_models},
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 10:09:08 AM*

**[REMOVED]**
```
(from line ~68)
top_models = filtered["Model"].value_counts().nlargest(5)

```
**[ADDED]**
```
68    top_models = filtered["Model"].value_counts().nlargest()
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 10:08:39 AM*

**[REMOVED]**
```
(from line ~80)
        value=f"KM {avg_mileage:,.0f}",

```
**[ADDED]**
```
80            value=f"Km {avg_mileage:,.0f}",
```
**[REMOVED]**
```
(from line ~83)
        
        

```
**[ADDED]**
```
84    with col3:
85        st.metric(
86            label="Top Models",
87            value=f"{top_models}",
88            delta=f"Region {top_region}"
89        )
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 10:06:47 AM*

**[REMOVED]**
```
(from line ~81)
        delta=f"Max mileage:{max_mileage} Min mileage {min_mileage}",

```
**[ADDED]**
```
81            delta=f"Max mileage:{max_mileage}   Min mileage {min_mileage}",
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 10:06:03 AM*

**[ADDED]**
```
77    with col2:
78        st.metric(
79            label=" Average Mileage (KM)",
80            value=f"KM {avg_mileage:,.0f}",
81            delta=f"Max mileage:{max_mileage} Min mileage {min_mileage}",
82            
83            
84            
85        )
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 10:02:15 AM*

**[REMOVED]**
```
(from line ~63)
avg_price =filtered['Avg_Price_USD']

```
**[ADDED]**
```
63    avg_price =filtered['Avg_Price_USD'].mean()
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 10:01:14 AM*

**[REMOVED]**
```
(from line ~74)
    st.metric("Avg Sales Price (USD)", f"${avg_price:,.0f}", delta=f"Max: ${max_price:,.0f}")

```
**[ADDED]**
```
74        st.metric(label="Avg Sales Price (USD)",
75        value=f"${avg_price:,.0f}",
76        delta=f"Max: ${max_price:,.0f}",)
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 9:59:26 AM*

**[REMOVED]**
```
(from line ~74)
    st.metric("AVG price (USD)", f"${avg_price:,.2f}", delta=f"Max: ${max_price}")
```
**[ADDED]**
```
74        st.metric("Avg Sales Price (USD)", f"${avg_price:,.0f}", delta=f"Max: ${max_price:,.0f}")
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 9:58:18 AM*

**[REMOVED]**
```
(from line ~74)
    st.metric("AVG price (USD)", f"${avg_price:.2f}", delta=f"Max: ${max_price}")
```
**[ADDED]**
```
74        st.metric("AVG price (USD)", f"${avg_price:,.2f}", delta=f"Max: ${max_price}")
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 9:57:57 AM*

**[REMOVED]**
```
(from line ~74)
    st.metric("AVG price (USD)", f"${avg_price}", delta=f"Max: ${max_price}")
```
**[ADDED]**
```
74        st.metric("AVG price (USD)", f"${avg_price:.2f}", delta=f"Max: ${max_price}")
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 9:57:16 AM*

**[REMOVED]**
```
(from line ~74)
    st.metric("AVG price (USD)", f"${avg_price:,.0f}", delta=f"${max_price:, .0f}")
```
**[ADDED]**
```
74        st.metric("AVG price (USD)", f"${avg_price}", delta=f"Max: ${max_price}")
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 9:55:40 AM*

**[REMOVED]**
```
(from line ~74)
    st.metric("AVG price (USD)", f"${avg_price:,.0f}", delta=)
```
**[ADDED]**
```
74        st.metric("AVG price (USD)", f"${avg_price:,.0f}", delta=f"${max_price:, .0f}")
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 9:54:41 AM*

**[REMOVED]**
```
(from line ~71)
st.write("#### 🔑 Key Performance Indicators")
```
**[ADDED]**
```
71    st.write("#### 🔑 Key Performance Indicators")
72    col1,col2,col3 =st.columns(3)
73    with col1:
74        st.metric("AVG price (USD)", f"${avg_price:,.0f}", delta=)
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 9:51:39 AM*

**[REMOVED]**
```
(from line ~70)
top_colors = filtered["Color"].value_counts().nlargest(3)

```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 9:51:29 AM*

**[REMOVED]**
```
(from line ~70)
top_colors = filtered["Color"].value_counts().nlargest(3)
```
**[ADDED]**
```
70    top_colors = filtered["Color"].value_counts().nlargest(3)
71    
72    st.write("#### 🔑 Key Performance Indicators")
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 9:51:09 AM*

**[REMOVED]**
```
(from line ~67)
max_mileage = filtered["Range_km"].max()
```
**[ADDED]**
```
67    max_mileage = filtered["Range_km"].max()
68    top_models = filtered["Model"].value_counts().nlargest(5)
69    top_region = filtered["Region"].value_counts().idxmax()
70    top_colors = filtered["Color"].value_counts().nlargest(3)
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 9:50:39 AM*

**[REMOVED]**
```
(from line ~65)
avg_mileage = filtered["Mileage_KM"].mean()
min_mileage = filtered["Mileage_KM"].min()
max_mileage = filtered["Mileage_KM"].max()
```
**[ADDED]**
```
65    avg_mileage = filtered["Range_km"].mean()
66    min_mileage = filtered["Range_km"].min()
67    max_mileage = filtered["Range_km"].max()
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 9:50:11 AM*

**[ADDED]**
```
65    avg_mileage = filtered["Mileage_KM"].mean()
66    min_mileage = filtered["Mileage_KM"].min()
67    max_mileage = filtered["Mileage_KM"].max()
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 9:49:52 AM*

**[ADDED]**
```
64    max_price =filtered['Avg_Price_USD'].max()
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 9:47:58 AM*

**[REMOVED]**
```
(from line ~63)
avg_price =filtered['']
```
**[ADDED]**
```
63    avg_price =filtered['Avg_Price_USD']
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 9:47:05 AM*

**[REMOVED]**
```
(from line ~59)
    
```
**[ADDED]**
```
59        
60        
61        ##Metrics kpis
62        
63    avg_price =filtered['']
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 9:45:37 AM*

**[REMOVED]**
```
(from line ~33)
Source_Type=st.sidebar.selectbox("Month", Month)

```
**[ADDED]**
```
33    selected_Month=st.sidebar.selectbox("Month", Month)
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 9:45:04 AM*

**[REMOVED]**
```
(from line ~33)
selected_Month=st.sidebar.selectbox("Month", Month)

```
**[ADDED]**
```
33    Source_Type=st.sidebar.selectbox("Month", Month)
```
**[ADDED]**
```
37    
```
**[ADDED]**
```
40    
41    ##applying filters
42    filtered =df.copy()
43    if selected_Model !="ALL":
44        filtered=filtered[filtered["Model"]== selected_Model]
45    if selected_region !="ALL":
46        filtered=filtered[filtered["Region"]== selected_region]  
47    
48    if selected_Source_Type !="ALL":
49        filtered=filtered[filtered["Source_Type"]== selected_Source_Type]  
50        
51    if selected_Month !="ALL":
52        filtered=filtered[filtered["Month"]== selected_Month]  
53        
54    if selected_year !="ALL":
55        filtered=filtered[filtered["Year"]== selected_year]  
56    
57    
58    filtered=filtered[(filtered['Range_km']>=KM_range[0]) & (filtered['Range_km']<=KM_range[1])]
59        
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 9:37:14 AM*

**[REMOVED]**
```
(from line ~37)
min_km, max_km =int(df[""])

```
**[ADDED]**
```
37    min_km, max_km =int(df["Range_km"].min()), int(df["Range_km"].max())
38    KM_range =st.sidebar.slider("Kilometre Range", min_km,max_km,(min_km,max_km))
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 9:35:17 AM*

**[REMOVED]**
```
(from line ~37)

region =["ALL"]+sorted(df['Region'].dropna().unique().tolist())
selected_region=st.sidebar.selectbox("Region", region)

region =["ALL"]+sorted(df['Region'].dropna().unique().tolist())
selected_region=st.sidebar.selectbox("Region", region)


```
**[ADDED]**
```
37    min_km, max_km =int(df[""])
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 9:32:57 AM*

**[REMOVED]**
```
(from line ~35)
region =["ALL"]+sorted(df['Region'].dropna().unique().tolist())
selected_region=st.sidebar.selectbox("Region", region)

```
**[ADDED]**
```
35    Source_Type =["ALL"]+sorted(df['Source_Type'].dropna().unique().tolist())
36    selected_Source_Type=st.sidebar.selectbox("Source Type", Source_Type)
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 9:32:16 AM*

**[REMOVED]**
```
(from line ~32)
region =["ALL"]+sorted(df['Region'].dropna().unique().tolist())
selected_region=st.sidebar.selectbox("Region", region)

```
**[ADDED]**
```
32    Month =["ALL"]+sorted(df['Month'].dropna().unique().tolist())
33    selected_Month=st.sidebar.selectbox("Month", Month)
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 9:31:49 AM*

**[REMOVED]**
```
(from line ~29)
region =["ALL"]+sorted(df['Region'].dropna().unique().tolist())
selected_region=st.sidebar.selectbox("Region", region)

```
**[ADDED]**
```
29    Model =["ALL"]+sorted(df['Model'].dropna().unique().tolist())
30    selected_Model=st.sidebar.selectbox("Model", Model)
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 9:31:27 AM*

**[REMOVED]**
```
(from line ~26)
region =["ALL"]+sorted(df['Region'].dropna().unique().tolist())
selected_region=st.sidebar.selectbox("Region", region)

```
**[ADDED]**
```
26    Year =["ALL"]+sorted(df['Year'].dropna().unique().tolist())
27    selected_year=st.sidebar.selectbox("Year", Year)
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 9:30:55 AM*

**[ADDED]**
```
26    region =["ALL"]+sorted(df['Region'].dropna().unique().tolist())
27    selected_region=st.sidebar.selectbox("Region", region)
28    
29    region =["ALL"]+sorted(df['Region'].dropna().unique().tolist())
30    selected_region=st.sidebar.selectbox("Region", region)
31    
32    region =["ALL"]+sorted(df['Region'].dropna().unique().tolist())
33    selected_region=st.sidebar.selectbox("Region", region)
34    
35    region =["ALL"]+sorted(df['Region'].dropna().unique().tolist())
36    selected_region=st.sidebar.selectbox("Region", region)
37    
38    region =["ALL"]+sorted(df['Region'].dropna().unique().tolist())
39    selected_region=st.sidebar.selectbox("Region", region)
40    
41    region =["ALL"]+sorted(df['Region'].dropna().unique().tolist())
42    selected_region=st.sidebar.selectbox("Region", region)
43    
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 9:30:08 AM*

**[REMOVED]**
```
(from line ~23)
region =["ALL"]+sorted(df[''])

```
**[ADDED]**
```
23    region =["ALL"]+sorted(df['Region'].dropna().unique().tolist())
24    selected_region=st.sidebar.selectbox("Region", region)
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 9:28:25 AM*

**[ADDED]**
```
23    region =["ALL"]+sorted(df[''])
```
**[REMOVED]**
```
(from line ~25)


```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 9:27:48 AM*

**[ADDED]**
```
23    
24    
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 9:27:18 AM*

**[REMOVED]**
```
(from line ~19)
st.dataframe(df)
```
**[ADDED]**
```
19    
20    ##sidebar filters
21    
22    st.sidebar.header("Filter Application")
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 9:25:23 AM*

**[REMOVED]**
```
(from line ~18)
df =load_data()
```
**[ADDED]**
```
18    df =load_data("Tesla2015-25.csv")
19    st.dataframe(df)
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 9:24:59 AM*

**[REMOVED]**
```
(from line ~9)
st.write("### From 2015 - 2025")
```
**[ADDED]**
```
9     st.write("### From 2015 - 2025")
10    
11    ##cache load data
12    
13    @st.cache_data
14    def load_data(path):
15        df=pd.read_csv(path)
16        return df  
17    
18    df =load_data()
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 9:22:52 AM*

**[REMOVED]**
```
(from line ~8)
st.title("T")
```
**[ADDED]**
```
8     st.title("Tesla Global Deliveries and Production Dashboard")
9     st.write("### From 2015 - 2025")
```

---

### 📄 c:\Users\Administrator\Desktop\Tesla dashboard\app.py
*Saved at: 11/19/2025, 9:21:58 AM*

**[ADDED]**
```
1     import streamlit as st   
2     import pandas as pd  
3     import plotly.express as px 
4     import numpy as np 
5     
6     
7     st.set_page_config(page_title="TESLA DASHBOARD", layout='wide')
8     st.title("T")
```

---

