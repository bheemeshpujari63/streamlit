import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Title and Description
st.title("Iris Flower Species Predictor 🌸")
st.write("Adjust the sliders to input flower measurements and predict the species.")

# Load Data Function with Caching
@st.cache_data
def load_data():
    """Load and cache the Iris dataset."""
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    return df, iris.target_names

# Load dataset
df, target_names = load_data()

# Train Model
model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df['target'])

# User Input Sliders
sepal_length = st.slider('Sepal Length (cm)', float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()), float(df['sepal length (cm)'].mean()))
sepal_width = st.slider('Sepal Width (cm)', float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()), float(df['sepal width (cm)'].mean()))
petal_length = st.slider('Petal Length (cm)', float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()), float(df['petal length (cm)'].mean()))
petal_width = st.slider('Petal Width (cm)', float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()), float(df['petal width (cm)'].mean()))

# Predict Button
if st.button("Predict Species"):
    input_data = np.array([sepal_length, sepal_width, petal_length, petal_width]).reshape(1, -1)
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    # Display Results
    st.write(f"### 🌿 The predicted species is **{target_names[prediction[0]]}**")
    
    # Show probability distribution for all species
    st.write("### 🔍 Prediction Probabilities")
    prob_df = pd.DataFrame(probability, columns=target_names)
    st.dataframe(prob_df.T.rename(columns={0: "Probability"}))


