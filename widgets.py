import streamlit as st
import pandas as pd



st.title('Hello Streamlit')
name = st.text_input('Enter your name')

age = st.slider('Enter your age', 0, 100, 25)
st.write(f'Your age is {age}')
if name:
    st.write(f'Hello {name}')
    
options = ["Python", "Java", "C++"]
language = st.selectbox('Which programming language do you use?', options)
st.write(f'You selected {language}')

df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 20, 30, 40, 50]
})
df.to_csv('data.csv', index=False)
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)