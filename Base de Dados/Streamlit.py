# Importações
import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
import numpy as np

# python -m streamlit run Streamlit.py

# Configurações & setup
st.set_page_config(page_title="Dashboard de Dengue", layout='wide')

df_base = pd.read_excel("Base_Final.xlsx")

st.title("🦟 🗑️ Relação entre os casos de dengue e o acúmulo de lixo nos municípios de São Paulo")

st.sidebar.header('Selecione os filtros')



filtroMes = st.sidebar.selectbox(
    "Mes",
    options=df_base['Mês'].unique()
)

filtroAno = st.sidebar.selectbox(
    "Ano",
    options=df_base['Ano'].unique()
)

filtroMunicipio = st.sidebar.selectbox(
    "Municipio",
    options=df_base['município'].unique()
)

st.write(f"Exibindo dados de *{filtroMunicipio}, do mês de *{filtroMes}*, do ano *{filtroAno}**")

df_selecao = df_base("Mês in @Mes and Ano in @Ano and município in @Municipio")

def Home():
    total_casos = df_base["qntd_casos"].sum()
    total_residuos = df_base["Peso total dos resíduos (kg)"].sum()

    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Total de Casos", value=int(total_casos))
    with col2:
        st.metric(label="Peso dos Resíduos (KG)", value=int(total_residuos))

    st.markdown("-----")


#Home()

# Gráficos

def Graficos():
    #Criar gráfico de barras, mostrando quantidade de produtos por loja
    fig_barras = px.bar(
        df_selecao, 
        x="Mês" + "/" + "Ano",
        y="Total de Casos",
        color="Mes",
        barmode="group",
        title="Total de casos por mes"
    )