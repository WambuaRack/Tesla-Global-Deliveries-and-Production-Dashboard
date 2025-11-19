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

