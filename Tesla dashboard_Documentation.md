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

