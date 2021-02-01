import streamlit as st
import pandas as pd

df = pd.read_csv("airbnb.csv")
st.write(df)