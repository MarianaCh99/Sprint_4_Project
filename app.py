import streamlit as st
import pandas as pd
import plotly.express as px

cars_df= pd.read_csv("vehicles_us.csv")

st.title("Anuncios de Ventas de Coches")

hist_button = st.button('Construir histograma') 
        
if hist_button: 
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    fig = px.histogram(cars_df, x="odometer")
        
    st.plotly_chart(fig, use_container_width=True)

graphic_button = st.button('Gráfico de dispersión') 

        
if graphic_button: 
    st.write('Creación de un gráficó de dispersión para el conjunto de datos de anuncios de venta de coches')
            
    fig = px.histogram(cars_df, x="odometer")
        
    st.plotly_chart(fig, use_container_width=True)

