# Importações
import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
import numpy as np


# python -m streamlit run Dash_Dengue.py


# Configuração da página
st.set_page_config(page_title="Dashboard de Dengue", layout='wide')

# Leitura da base
df_base = pd.read_excel("Streamlit_Dengue/Base_Final.xlsx")

# Título
st.title("🦟 🗑 Relação entre os casos de dengue e o acúmulo de lixo nos municípios de São Paulo")

# Filtros
st.sidebar.header('Selecione os filtros')

filtroMes = st.sidebar.multiselect(
    "Mês",
    options= df_base["Mês"].unique(),
    default = df_base["Mês"].unique(),
)

filtroAno = st.sidebar.multiselect(
    "Ano",
    options=df_base["Ano"].unique(),
    default = df_base["Ano"].unique(),
)

#filtrodata = st.sidebar.multiselect(
   # "Data",
    #options=df_base["dt_notificacao"].unique(),
    #default= df_base["dt_notificacao"].unique(),
#)

filtroMunicipio = st.sidebar.multiselect(
    "Município",
    options=df_base["município"].unique(),
    default = df_base["município"].unique(),
)


# Filtro no DataFrame
df_selecao = df_base[
    (df_base["Mês"].isin(filtroMes)) &
    (df_base["Ano"].isin(filtroAno)) &
    #(df_base["dt_notificacao"].isin(filtrodata)) &
    (df_base["município"].isin(filtroMunicipio))
]

# Página Home
def Home():
    total_casos = df_selecao["qntd_casos"].sum()
    total_residuos_peso = df_selecao["Peso total dos resíduos (kg)"].sum()
    total_residuos_qtd = df_selecao["Quantidade total de itens coletados:     "].sum()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Total de Casos", value=int(total_casos))
    with col2:
        st.metric(label="Peso Total dos Resíduos (KG)", value=int(total_residuos_peso))
    with col3:
        st.metric(label="Quantidade Total de Resíduos", value=int(total_residuos_qtd))

    st.markdown("-----")

# Página de Gráficos
def Graficos():
    peso = px.bar(
        df_selecao,
        x="dt_notificacao",
        y="Peso total dos resíduos (kg)",
        color = "dt_notificacao",
        barmode = "group",
        title="Peso do lixo por data"
    )

    casos = px.bar(
        df_selecao,
        x="dt_notificacao",
        y="qntd_casos",
        color= "dt_notificacao",
        barmode = "group",
        title="Casos de dengue por data"
    )

    quantidade = px.bar(
        df_selecao,
        x="dt_notificacao",
        y="Quantidade total de itens coletados:     ",
        color= "dt_notificacao",
        barmode = "group",
        title="Quantidade de itens por data"
    )

    tipo_lixo = px.bar(
        df_selecao,
        x=["Garrafas PET","Pneus","Copos/talheres/pratos","Sacos e sacolas", "Latas de bebida","Caixas de leite/suco, etc"],
        y="dt_notificacao",
        # color= ["Garrafas PET","Pneus"],
        barmode = "group",
        title="Tipo de lixo por data"
    )

   

    # casos_linha = px.line(
    #     df_selecao,
    #     x="dt_notificacao",
    #     y=["qntd_casos","qntd_resultado_soro","qntd_resultado_ns1","qntd_resultado_pcr"],
    #     title="Casos de dengue por data"
    # )
    # tipo_teste = px.line(
    #     df_selecao,
    #     x="dt_notificacao",
    #     y=["qntd_resultado_soro","qntd_resultado_ns1","qntd_resultado_pcr"],
    #     #barmode = "group",
    #     title="Tipo de lixo por data"
    # )

    graf1, graf2 = st.columns(2)
    with graf1:
        st.plotly_chart(casos, use_container_width=True, font_size=50)
    with graf2:
        st.plotly_chart(peso, use_container_width=True, font_size=50)

    graf3, graf4 = st.columns(2)
    with graf3:
        st.plotly_chart(quantidade, use_container_width=True, font_size=50)
    with graf4:
        st.plotly_chart(tipo_lixo, use_container_width=True, font_size=50)
    # st.plotly_chart(tipo_teste, use_container_width=True)

# Sidebar com menu
def sidebar():
    with st.sidebar:
        selecionado = option_menu(
            menu_title="Menu",
            options=["Home", "Gráficos"],
            icons=["house", "bar-chart"],
            default_index=0
        )

    if selecionado == "Home":
        Home()
        Graficos()
    elif selecionado == "Gráficos":
        Graficos()

# Executa a sidebar/menu
sidebar()
