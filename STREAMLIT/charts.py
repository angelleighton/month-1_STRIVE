import streamlit as st
import numpy as np
import pandas as pd

st.title('MY WEB APP')
st.write('table')

#TABLE
data = pd.DataFrame(np.random.randn(10, 20), 
    columns = ('col %d' % i
        for i in range(20)))
st.write(data)

#LINE CHART
st.write('line chart')
st.line_chart(data)

#AREA CHART
st.write('area chart')
st.area_chart(data)


#HISTOGRAM
st.write('Histogram')
st.bar_chart(data)

#MAP
st.write('Map')
df = pd.DataFrame(
    np.random.randn(1000, 2) / [60, 60] + [36.66, -121.6],
    columns = ['latitude', 'longitude'])

st.map(df)

#BASE CONDA PATH
