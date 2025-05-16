import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px


#python -m streamlit run Streamlit_Treinamento.py


st.set_page_config(page_title="Dashboard Despesas", layout="wide")

df = pd.read_excel("Orcamento_Tratado.xlsx")

df["Valor"] = df["Valor"].astype("float")

st.sidebar.header("Selecione os filtros")

df["Valor"] = df["Valor"].astype("float")
#Setor / Tipo / Data / Fornecedor
setores = st.sidebar.multiselect(
    "Setores",
    options = df["Setor"].unique(),
    default = df["Setor"].unique(),
    key = "setores"
)

tipos = st.sidebar.multiselect(
    "Tipos Despesas",
    options = df["Tipo"].unique(),
    default = df["Tipo"].unique(),
    key = "tipos"
)

fornecedor = st.sidebar.multiselect(
    "Fornecedores",
    options = df["Fornecedor"].unique(),
    default = df["Fornecedor"].unique(),
    key = "fornecedor"
)

data = st.sidebar.multiselect(
    "Datas",
    options = df["Data"].unique(),
    default = df["Data"].unique(),
    key = "data"
)

#trimestre = st.sidebar.multiselect(
    #"Trimestre",
    #options = df["Trimestre"].unique(),
    #default = df["Trimestre"].unique(),
    #key = "trimestre"
#)



df_selecao = df.query("Setor in @setores and Tipo in @tipos and Fornecedor in @fornecedor and Data in @data")

def Home():
    st.title("Analise de Despesas")

    total_Despesas = df["Valor"].sum()
    #media_despesas_setor = df.groupby("Setor")["Valor"].mean()

    total1 = st.columns(1)[0]

    #with total1:
    st.metric("Total Despesas", value= float(total_Despesas))

    #with total2:
        #st.metric("Média Despesas por Mês", value= media_despesas_setor)

    st.markdown("---")


def Graficos():
    salario_area = px.bar(
        df_selecao,
        x="Setor",
        y="Valor",
        color="Setor",
        barmode = "group",
        title = "Salário por Setor"
    )



    st.columns(1)

    #with graf1:
    st.plotly_chart(salario_area, use_container_width=True)


def sidebar():
    with st.sidebar:
        selecionado = option_menu(
            menu_title= "Menu",
            options = ["Home", "Graficos"],
            icons= ["house", "bar-chart"],
            default_index=0
        )

        if selecionado == "Home":
            Home()
            Graficos()
        elif selecionado == "Graficos":
            Graficos()

sidebar()


