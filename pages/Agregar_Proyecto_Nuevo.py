from datetime import time
import datetime
import streamlit as st


currency="Proyectos"
page_title = "Socio formadores"
page_icon=":office_worker:"
layout= "centered"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title+""+page_icon)

st.header(f"Registro de {currency}")
name= st.text_input("Nombre del proyecto: ")
 
##Descripción del proyecto##
with st.expander("Información del proyecto "):
  st.header("Descripción")
  description= st.text_area("Objetivos:", placeholder="Ingrese aquí los objetivos o la descripción del proyecto...")
 
  ##Cupo del grupo
  NumAl = st.number_input("Número de alumnos requeridos: ", min_value=1, format="%i", step= 1)

  ##Horas a acreditar##
  horAc = st.number_input("Cantidad máxima de horas a acreditar: ", min_value=40, format="%i", step= 1)
  
  ##Requisitos
  st.header("Requisitos")
  
  ##Carreras
  carreras=st.multiselect("Seleccione las carreras participantes: ", ["Todas","Arquitecto", "Ingeniero Civil","Licenciado en Urbanismo""Licenciado en economía", "Licenciado en Derecho","Licenciado en Relaciones Internacionales", "Licenciado en Gobierno y transformación pública", "Licenciado en Arte digital","Licenciado en Comunicación","Licenciado en Diseño","Licenciado en Innovación Educativa","Licenciado en Letras Hispanicas","Licenciado en periodismo","Licenciado en Tecnología y producción musical","Ingeniero Biomedico", "Ingeniero en Electronica", "Ingeniero en innovacion y desarrollo","Ingeniero industrial y de sistemas","Ingeniero Mecanico","Ingniero Mecatronico"])

  ##Habilidades
  requirements = st.text_area("Ingrese las habilidades del alumno o los requisitos necesarios, uno por línea")
  requirements = requirements.split("\n")
  requirements = list(filter(None, requirements))
  if len(requirements) > 0:
    st.write("Requisitos:")
    for i, requirement in enumerate(requirements):
      st.write(f"{i+1}. {requirement}")
  
  ##Fechas y horario
  st.header("Fechas y horario de servicio")
  
  ##Fechas
  today = datetime.date.today()
  tomorrow = today + datetime.timedelta(days=1)
  start_date = st.date_input('Fecha de inicio', today)
  end_date = st.date_input('Fecha de término', tomorrow)

  ##Horario
  #Tiempo de inicio y término por defecto
  start_time = time(8, 0)
  end_time = time(18, 0)

  #Rango de tiempo seleccionable por el usuario
  selected_time_range = st.slider("Seleccione el rango de tiempo", value=(start_time, end_time), format="HH:mm")

  timePro = selected_time_range[0].strftime("%H:%M")
  #Mostrar el rango de tiempo seleccionado
  st.write("Rango de tiempo seleccionado: {} - {}".format(selected_time_range[0].strftime("%H:%M"), selected_time_range[1].strftime("%H:%M")))

  ##Modalidad
  modalidad= ["Presencial", "Remoto", "Híbrido"]
  tipoS = st.selectbox("Seleccione la modalidad",modalidad,key="Modalidad")

  ##Dirección
  st.header("Dirección")
  # Calle y Número
  calle_numero = st.text_input("Calle y Número")

  # Colonia
  colonia = st.text_input("Colonia")

  # Ciudad, Estado y Código Postal
  col1, col2, col3 = st.columns([2,1,2])
  with col1:
      ciudad = st.text_input("Ciudad")
  with col2:
      estado = st.selectbox("Estado", ["", "Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Chiapas", "Chihuahua", "Coahuila", "Colima", "Ciudad de México", "Durango", "Estado de México", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco", "Michoacán", "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro", "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatán", "Zacatecas"])
  with col3:
      codigo_postal = st.text_input("Código Postal")

  direccion = ciudad + estado + codigo_postal

  act = st.text_area("Ingrese las actividades, una por línea")
  act = act.split("\n")
  act = list(filter(None, act))
  if len(requirements) > 0:
   st.write("Actividades:")
   for i, act in enumerate(act):
    st.write(f"{i+1}. {act}")

  entre = st.text_area("Ingrese los entregables, uno por línea")
  entre = entre.split("\n")
  entre = list(filter(None, entre))
  if len(entre) > 0:
    st.write("Entregables:")
    for i, entre in enumerate(entre):
      st.write(f"{i+1}. {entre}")
  numEnt = len(entre)
## Costo
with st.expander("Costo"):
  costo = st.number_input("Costo de participación: ", min_value=0, format="%i", step= 1)
  motivoCost= st.text_area("Motivo del costo:",placeholder="Ingrese el motivo del costo...")

 
## Medio de contacto
with st.expander("Contacto de la organización"):
  responsable= st.text_input("Nombre del responsable",placeholder="Ingrese el nombre del responsable")
  col3, col4 = st.columns([2,2])
  with col3:
    num_tel= st.text_input("Número de teléfono",placeholder="Ingrese su número de teléfono")
  with col4:
    correo= st.text_input("Correo electrónico",placeholder="Ingrese su correo electrónico")
  sitio_web= st.text_input("Sitio web",placeholder="Ingrese la URL del sitio web o de la página de red social")

#Agregar proyecto a Firebase

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

# Use a service account.
if not firebase_admin._apps:
   cred = firebase_admin.credentials.Certificate('/Users/antoniopatjane/Downloads/prueba-a5c60-firebase-adminsdk-x4i46-fa094b7b92.json')
   default_app = firebase_admin.initialize_app(cred, {
	   'databaseURL':'https://prueba-a5c60-default-rtdb.firebaseio.com/'
	   })

from firebase_admin import db

refOrg = db.reference("/Organizaciones/Aprendamos Juntos/")
if st.button('Guardar Proyecto'):
  refOrg.push({    name :
              {
                  "Descripcion":
                      {
                          "Descripcion": description,
                          "Numero de alumnos": NumAl,
                          "Horas acreditar": horAc,
                          "Carreras": carreras,
                          "Habilidades del alumno": requirements,
                          "Fecha de inicio": str(start_date),
                          "Fecha de termino": str(end_date),
                          "Horario": ("{} - {}".format(selected_time_range[0].strftime("%H:%M"), selected_time_range[1].strftime("%H:%M"))),
                          "Modalidad": tipoS,
                          "Direccion": direccion,
                          "Actividades": act,
                          "Entregables": entre,
                          "Costo": costo,
                          "Motivo de costo": motivoCost,
                          "Nombre del responsable": responsable,
                          "Numero de teléfono": num_tel,
                          "Correo": correo,
                          "Sitio web": sitio_web
                      },

                  "Alumnos":
                  {
                     "Alumno Prueba":
                    {
                        "Matricula": "A000000",
                        "Semana de Induccion": "Si",
                        "Semestre": 1,
                        "Estatus de Entrevista": "En proceso",
                        "Horas Acreditadas": "0",
                        "Correo": ""
                    }
                  }
              }
            })
else:
  st.write('Proyecto no guardado')

