import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import numpy as np

# Title of the application

st.title('Hello Streamlit')

# Display a simple text
st.write('This is a simple text')

#create a dataframe
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 20, 30, 40, 50]
})

# Display the dataframe
st.write(df)

#create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
# Display a line chart
st.line_chart(chart_data)