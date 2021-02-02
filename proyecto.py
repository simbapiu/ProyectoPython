# ====== Imports ======
import streamlit as st
import pandas as pd
import numpy as np
import plotly
import plotly.express as px
import plotly.io as pio
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from PIL import Image

# ====== Proyecto Airbnb equipo 2 ======

df = pd.read_csv("airbnb.csv")
dfFiltrado = df.sort_values(["availability_365", "number_of_reviews"], ascending = [True, False])

# ====== Filtros del Dataframe "df" ======

# ***** Filtro de Rich *****
vecindarios = np.append(["Selecciona un vecindario"], df["neighbourhood_group"].unique())
filter_NHG = st.sidebar.selectbox("Vecindario", vecindarios)


if filter_NHG != 'Selecciona un vecindario':
    dfFiltrado = dfFiltrado[dfFiltrado["neighbourhood_group"] == filter_NHG]

# ====== Estructura de la Page =======
st.title("Airbnb: Alojamientos")
st.header("Ciudad de Nueva York")

# ***** Apartado de de Franz *****
st.subheader("Tipos de alojamiento mas demandados")
st.text("Nueva York es una de las ciudades con mayor costo para vivir. \n" +
        "Dicho hecho es el influyente en los altos costos de vivienda al igual que la falta de \n" +
        "disponibilidad de suelo, por ende el tipo de alojamiento mas ofertado es: apartamentos, \n" +
        "sin embargo la otra mitad de la oferta son cuartos mas un pequeño porcentaje de cuartos \n" +
        "compartidos y cuartos de hotel")

f1 = df.groupby(['room_type']).size().reset_index(name='Count')
fig = px.pie(f1, values=f1["Count"], names=f1["room_type"], title='Distribución de alojamientos')
st.plotly_chart(fig)

# ------ Vecindario con mayor número de alojamientos ------ #
st.subheader("Número de alojamientos en los vecindarios")
st.text("En la siguiente tabla, podemos observar que Manhattan es el vecindario \n" +
        "con mayor número de alojamientos, con un total de 21,183 alojamientos.")

f1 = df.groupby(['neighbourhood_group']).size().reset_index(name='Count')
fig = go.Figure(data=[go.Bar(name='Confirmed', x=f1['neighbourhood_group'], y=f1['Count'])])
st.plotly_chart(fig)
    
# ***** Apartado de de Rich *****

# Top Alojamientos
st.subheader("Top 5 de Alojamientos")
st.text("Actualmente, al tratar de elegir un alojamiento, no solamente nos interesa el precio, \n" +
        "también, buscamos opiniones acerca de los demás usuarios y aquí es donde entra la \n" + 
        "popularidad de alojamientos. \n" +
        "¿Por qué la popularidad de alojamientos? ya sea por saber qué colonia tiene mayor \n" + 
        "inquilinos o qué colonia tiene los alojamientos mas rentados. Por eso acontinuación, \n" + 
        "te listamos el top 5 de alojamientos en la ciudad de Nueva York")
st.text("*Las imagenes son ilustrativas*")

filtro_NH = 'Selecciona una colonia'

if filter_NHG != 'Selecciona un vecindario':
    colonias = np.append([filtro_NH], dfFiltrado["neighbourhood"].unique())
    filtro_NH = st.sidebar.selectbox("Colonia", colonias)
    
    if filtro_NH != 'Selecciona una colonia' :
        nh_filtrado = dfFiltrado[dfFiltrado['neighbourhood'] == filtro_NH]    

# Load top images
image1 = Image.open('images/alojamiento_top1.jpeg')
image2 = Image.open('images/alojamiento_top2.jpeg')
image3 = Image.open('images/alojamiento_top3.png')
image4 = Image.open('images/alojamiento_top4.jpeg')
image5 = Image.open('images/alojamiento_top5.jpeg')

images = [image1, image2, image3, image4, image5]

if filtro_NH != 'Selecciona una colonia' :
    top_5 = nh_filtrado.head()
    top_5['images'] = images
    st.image(list(top_5['images']), caption=list(top_5['name']), width=64, use_column_width=True)
else:
    top_5 = dfFiltrado.head()
    st.image(images, caption=list(top_5['name']), width=64, use_column_width=True)
    
# Distribución de precios por alojamiento
st.subheader("Distribución de los precios por alojamiento y vecindario")
st.text("La siguiente gráfica nos muestra la distribución de los tipos de alojamientos \n" + 
        "de acuerdo a su precio (eje x) y la cantidad de alojamientos de ese tipo (eje y).")

df2 = df.groupby(['room_type', 'price', 'neighbourhood_group']).size().reset_index(name='Count')
df2 = df2.sort_values('price')

fig = px.scatter(df2, x="price", y="Count", size="price", color="room_type", 
                 hover_name="neighbourhood_group", log_x=True, size_max=60)

#fig["layout"].pop("updatemenus") # optional, drop animation buttons
st.plotly_chart(fig)

# Mapa de distribución de alojamientos. Filtrados por Neighborhood, Precio, Reviews

st.subheader("Distribución de alojamientos")
st.text("Existen varios tipos de alojamientos, tal vez nos sea indistinto si queremos \n" +
        "alguna casa completa, si un cuarto o hasta una habitación de hotel, pero lo primero \n" + 
        "que miramos en un alojamiento es su ubicación y su precio. \n" +
        "A continuación, podremos observar en el mapa la distribución de los alojamientos \n" + 
        "de acuerdo a su colonia y a un rango de precio.")

if filter_NHG != "Selecciona un vecindario":
    if filtro_NH != 'Selecciona una colonia' :
        filterPrice = st.slider("Filtrar por precio", nh_filtrado['price'].min(), nh_filtrado['price'].max(), [0, nh_filtrado['price'].max()])
        st.map(nh_filtrado[(nh_filtrado['price'] >= filterPrice[0]) & (nh_filtrado['price'] <= filterPrice[1])])
    else:
        filterPrice = st.slider("Filtrar por precio", dfFiltrado['price'].min(), dfFiltrado['price'].max(), [0, dfFiltrado['price'].max()])
        st.map(dfFiltrado[(dfFiltrado['price'] >= filterPrice[0]) & (dfFiltrado['price'] <= filterPrice[1])])
else:
    filterPrice = st.slider("Filtrar por precio", df['price'].min(), df['price'].max(), [0, df['price'].max()])
    st.map(df[(df['price'] >= filterPrice[0]) & (df['price'] <= filterPrice[1])])
