import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Vizualizaciones de conjunto de datos')

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_checkbox = st.checkbox('Construir histograma')  # crear un cheackbox

if hist_checkbox:  # al hacer clic en la caja
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

scat_button = st.button(
    'Construir un diagrama de dispersión')  # crear un cheackbox

if scat_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    # crear un gráfico de dispersión
    figu = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(figu, use_container_width=True)
