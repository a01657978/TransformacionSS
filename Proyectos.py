import pandas as pd
import time
import streamlit as st
import plotly.express as px


# Vista Socio Formador 

# Create the title for the web app


st.title("Aprendamos Juntos MTY")


#
#with open('/Users/antoniopatjane/Downloads/AJ.txt') as f:
#    OrgDesc = f.read()

container = st.container()
container.header('Sus proyectos son:')

tab1, tab2, tab3, tab4 = st.tabs(["Comunicacion(Español)", "Matematicas I", "Matematicas II", "Matematicas III"])

@st.cache_data
def load_dataset(data_link):
    dataset = pd.read_csv(data_link)
    return dataset

alumnos = pd.read_csv('/Users/antoniopatjane/Downloads/Proyecto SS/alumnos.csv')



with tab1:
   st.header("Alumnos")
   st.dataframe(alumnos)

   select_alumn = st.selectbox("Selecciona Alumno", alumnos['Nombre'].unique())
   select_alumn = select_alumn.replace("'", "")


   horas = st.slider(f'Cuantas horas acredito el Alumno: {select_alumn!r} ?', 0, 120, 60)
   st.write(f'El alumno {select_alumn!r} acredito', horas, 'horas con el proyecto')

   if st.button('Guardar'):
    st.write('Horas acreditadas')
    alumnos.at[select_alumn,'Grupo'] = horas
   else:
    st.write('Progreso no guardado')


with tab2:
   st.header("Alumnos")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("Alumnos")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

with tab4:
   st.header("Alumnos")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

st. subheader('Total de alumnos inscritos en la organizacion')
st.metric(label="Total:", value = len(alumnos.axes[0]), label_visibility='hidden' )