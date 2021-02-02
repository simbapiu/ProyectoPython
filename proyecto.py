# ====== Imports ======
import streamlit as st
import pandas as pd
import numpy as np
import plotly
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from PIL import Image

# ====== Proyecto Airbnb equipo 2 ======

dfGeneral = pd.read_csv("airbnb.csv")
df = dfGeneral.sort_values(["availability_365", "number_of_reviews"], ascending = [True, False])

# ====== Filtros del Dataframe "df" ======

# ***** Filtro de Rich *****
top_5 = df.head()
colonias = np.append(["Selecciona una colonia"], top_5["neighbourhood"].unique())

# ***** Filtro de Franz *****
vecindarios = np.append(["Selecciona un vecindario"], df["neighbourhood_group"].unique())
filter_NB = st.sidebar.selectbox("Vecindario", vecindarios)

# ====== Estructura de la Page =======
st.title("Airbnb: Alojamientos")
st.header("Ciudad de Nueva York")

# ***** Apartado de de Franz *****
st.subheader("Tipos de alojamiento mas demandados")
st.text("Nueva York es una de las ciudades con mayor costo para vivir. \n" +
        "Dicho hecho es el influyente en los altos costos de vivienda al igual que la falta de \n" +
        "disponibilidad de suelo, por ende los tipos de departamento mas ofertados son apartamentos, \n" +
        "sin embargo la otra mitad de la oferta son cuartos mas un pequeño porcentaje de cuartos \n" +
        "compartidos y cuartos de hotel")

f1 = df.groupby(['room_type']).size().reset_index(name='Count')
fig = px.pie(f1, values=f1["Count"], names=f1["room_type"], title='Distribución de alojamientos')
st.plotly_chart(fig)

if filter_NB != "Selecciona un vecindario":
    st.map(df[ df["neighbourhood_group"] == filter_NB] )

else:
    st.map(df)
    
# ***** Apartado de de Rich *****

# Title
st.subheader("Top 5 de Alojamientos")
st.text("Actualmente, al tratar de elegir un alojamiento, no solamente nos interesa el precio, \n" +
        "también, buscamos opiniones acerca de los demás usuarios y aquí es donde entra la \n" + 
        "popularidad de alojamientos. \n" +
        "¿Por qué la popularidad de alojamientos? ya sea por saber qué colonia tiene mayor \n" + 
        "inquilinos o qué colonia tiene los alojamientos mas rentados. Por eso acontinuación, \n" + 
        "te listamos el top 5 de alojamientos en la ciudad de Nueva York")
st.text("*Las imagenes son ilustrativas*")

filtro_NH = st.selectbox("Colonia", colonias)

# Load top images
image1 = Image.open('images/alojamiento_top1.jpeg')
image2 = Image.open('images/alojamiento_top2.jpeg')
image3 = Image.open('images/alojamiento_top3.png')
image4 = Image.open('images/alojamiento_top4.jpeg')
image5 = Image.open('images/alojamiento_top5.jpeg')

images = [image1, image2, image3, image4, image5]

top_5['images'] = images

if filtro_NH != 'Selecciona una colonia' :
    filter_values = top_5[top_5['neighbourhood'] == filtro_NH]
    st.image(list(filter_values['images']), caption=list(filter_values['name']), width=64, use_column_width=True)
else:
    st.image(images, caption=list(top_5['name']), width=64, use_column_width=True)