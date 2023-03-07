import pandas as pd
import time
import streamlit as st
import plotly.express as px
import json

# Vista Socio Formador 

# Create the title for the web app

# Firebase 


import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
if not firebase_admin._apps:
   cred = firebase_admin.credentials.Certificate('/Users/antoniopatjane/Downloads/prueba-a5c60-firebase-adminsdk-x4i46-fa094b7b92.json')
   default_app = firebase_admin.initialize_app(cred, {
	   'databaseURL':'https://prueba-a5c60-default-rtdb.firebaseio.com/'
	   })

from firebase_admin import db


st.title("Aprendamos Juntos MTY")
#
#with open('/Users/antoniopatjane/Downloads/AJ.txt') as f:
#    OrgDesc = f.read()

refPro = db.reference("/Organizaciones/Aprendamos Juntos")

container = st.container()
container.header('Sus proyectos son:')

#proyectosDisp = ref.get()




tab1, tab2 = st.tabs(["Comunicacion(Español)", "Matematicas I"])

@st.cache_data
def load_dataset(data_link):
    dataset = pd.read_csv(data_link)
    return dataset

#alumnos = pd.read_csv('/Users/antoniopatjane/Downloads/Proyecto SS/alumnos.csv')


with tab1:
   st.header("Alumnos")
   ref = db.reference("/Organizaciones/Aprendamos Juntos/Espanol/Alumnos")

   proyectosDisp = ref.get()

   f = pd.DataFrame.from_dict(proyectosDisp)
   alumnos = f.transpose()
   st.dataframe(alumnos)

   select_alumn = st.selectbox("Selecciona Alumno", alumnos.index)
   


   horas = st.slider(f'Cuantas horas acredito el Alumno: {select_alumn!r} ?', 0, 120, 60)
   st.write(f'El alumno {select_alumn!r} acredito', horas, 'horas con el proyecto')

   
   if st.button('Guardar'):
    st.write('Horas acreditadas')
    alumnos.at[select_alumn,'Grupo'] = horas
   else:
    st.write('Progreso no guardado')


with tab2:
      st.header("Alumnos")
      ref = db.reference("/Organizaciones/Aprendamos Juntos/Matematicas/Alumnos")

      proyectosDisp = ref.get()

      f = pd.DataFrame.from_dict(proyectosDisp)
      alumnos = f.transpose()
      st.dataframe(alumnos)

      select_alumn = st.selectbox("Selecciona Alumno", alumnos.index)
      select_alumn = select_alumn.replace("'", "")


      horas = st.slider(f'Cuantas horas acredito el Alumno: {select_alumn!r} ?', 0, 120, 60)
      st.write(f'El alumno {select_alumn!r} acredito', horas, 'horas con el proyecto')

      if st.button('Guardar '):
         st.write('Horas acreditadas')
         alumnos.at[select_alumn,'Grupo'] = horas
      else:
         st.write('Progreso no guardado')


st. subheader('Total de alumnos inscritos en la organizacion')
st.metric(label="Total:", value = len(alumnos.axes[0]), label_visibility='hidden' )