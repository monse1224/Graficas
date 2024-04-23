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

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.hist(titanic_data['Fare'])
st.header("Histograma del Titanic")
st.pyplot(fig)

fig2,ax2 =plt.subplots()
y_pos=titanic_data['Pclass']
x_pos=titanic_data['Fare']
ax2=barh(y_pos,x_pos)
ax2.set_ylabel('Class')
ax2.set_laxbel('Fare')
ax2.set_title('¿Cuánto pagaron las clases del titanic?')
st.header('Gráfica de barras del titanic')
st.pyplot(fig2)

fig3,ax3=plt.subplots()
ax3.scatter(titanic_data['Age'],titanic_data['Fare'])
ax3.set_xlabel('Edad')
ax3.set_xlabel('Tarifa')
st.header('Gráfica de dispersión del titanic')
st.pyplot(fig3)

fig4,ax4=plt.subplots()
ax4=titanic_data.boxplot(['Age'])
ax4.set_ylabel('Edad')
st.header('Gráfica de cajas por edad')
st.pyplot(fig4)



