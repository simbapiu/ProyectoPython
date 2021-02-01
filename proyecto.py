import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# Proyecto Airbnb equipo 2

df = pd.read_csv("airbnb.csv")
df = df.sort_values(["availability_365", "number_of_reviews"], ascending = [True, False])

# Filtros

top_5 = df.head()
colonias = np.append(["Selecciona una colonia"], top_5["neighbourhood"].unique())

# Title
st.title("Airbnb: Alojamientos")
st.header("Ciudad de Nueva York")
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