import pandas as pd
import streamlit as st
import numpy as np

st.title("Centros de vacunación contra el COVID19 en Perú")

df = pd.read_csv('TB_CENTRO_VACUNACION.csv')
names = {'id_centro_vacunacion':'ID_CentroVac',
         'id_ubigeo':'ID_Ubigeo',
         'nombre':'Nombre',
         'latitud':'lat',
         'longitud':'lon',
         'entidad_administra':'Entidad',
         'id_eess':'ESS'}
df = df.rename(columns=names)
option = st.selectbox(
    'Elija la sede que desea ver',
    df[['Nombre']])
st.write('Selecciono la opcion ',option)
st.map(df[df.Nombre == option][['lat','lon']])
