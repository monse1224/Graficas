#importamos la biblioteca
import streamlit as st

# creamos el titulo de la App
st.title("Titanic App")
st.header("Titanic Graphs App")
st.write("Graficas del titanic")

import pandas as pd
titanic_link='Titanic.csv'
titanic_data=pd.read_csv(titanic_link)
st.dataframe(titanic_data)