# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 16:13:59 2022

@author: lechu
"""

#import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit as st

# Title of aplication
st.set_page_config(page_title = 'Dashboard',
                   layout = 'wide')

df = pd.read_excel(
    io = 'PC_2022.xlsm',
    engine = 'openpyxl',
    sheet_name = 'Expansión_Fechas',
    usecols='A:F',
    nrows = 40
    )

# Print data base in app
#st.dataframe(df)


# -------- SIDEBAR 

st.sidebar.header('Seleccione el filtro')

contratista = st.sidebar.multiselect(
    'Seleccione el contratista:',
    options = df['Contratista'].unique(),
    default = df['Contratista'].unique(),
    )

rodal = st.sidebar.multiselect(
    'Seleccione el Rodal:',
    options = df['Rodal'].unique(),
    default = df['Rodal'].unique(),
    )

# Filter values of the df
df_selection = df.query(
    "Contratista == @contratista & Rodal == @rodal"  
    )



# -------- MAIN PAGE
st.title(':bar_chart: Dashboard de Producción')
st.markdown('##')

# Top KPI's

total_production = int(df_selection["Volumen"].sum())
star_ranting = ":star:" * 5


left_column, middle_column = st.columns(2)

with left_column:
    st.subheader('Producción total:')
    st.subheader(f'{total_production:,} m³')

with middle_column:
    st.subheader('Estrellas:')
    st.subheader(f"{star_ranting}")

# Print data base in app
st.dataframe(df_selection)






























