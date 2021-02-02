# ====== Imports ======
import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
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

# Group data together
f1 = df.groupby(['neighbourhood_group', 'neighbourhood']).size().reset_index(name='Count')

fBronx = f1[f1['neighbourhood_group']=='Bronx']
fManhattan = f1[f1['neighbourhood_group']=='Manhattan']
fSI = f1[f1['neighbourhood_group']=='Staten Island']
fQueens = f1[f1['neighbourhood_group']=='Queens']
fBrooklyn = f1[f1['neighbourhood_group']=='Brooklyn']

x1 = list(fBronx['Count'])
x2 = list(fManhattan['Count'])
x3 = list(fSI['Count'])
x4 = list(fQueens['Count'])
x5 = list(fBrooklyn['Count'])

hist_data = [x1, x2, x3, x4, x5]

group_labels = list(f1['neighbourhood_group'].unique())

# Create distplot with custom bin_size
fig = ff.create_distplot(hist_data, group_labels, bin_size=[1000, 2000, 3000, 4000])

# Plot!
st.plotly_chart(fig, use_container_width=True)

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