import streamlit as st
import pandas as pd

# Proyecto Airbnb equipo 2

df = pd.read_csv("airbnb.csv")
st.write(df)