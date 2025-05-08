#pip install streamlit
#pip install streamlit-option-menu
#pip install plotly.express
#python -m streamlit run projeto.py


import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px

#Configurações inicias

st.set_page_config(page_title="Dashboard Vendas", page_icon='💵💵💵',layout='wide')

#carregar dados

df = pd.read_excel("Vendas.xlsx")

#Filtros

#Sidebar
st.sidebar.header('Selecione os filtros')

#Filtro por loja
lojas = st.sidebar.multiselect(
#Opções filtro
    "Lojas", 
    options = df['ID Loja'].unique(),
#Opção que vem por padrão no filtro
    default = df['ID Loja'].unique(),
#Chave única
    key="loja"
)


#Filtro Produto
produtos = st.sidebar.multiselect(
    "Produtos", options= df['Produto'].unique(),
    default= df['Produto'].unique(),
    key='produto'
)

#Filtrar dataframe de acordo com as opções selecionadas
df_selecao = df.query("`ID Loja` in @lojas and Produto in @produtos")

#Gráficos e na função da página

def Home():
    st.title("Faturamento das lojas")

    total_vendas = df['Quantidade'].sum()
    media_vendas = df['Quantidade'].mean()
    mediana_vendas = df['Quantidade'].median()
    total_valor = df['Valor Final'].sum()
#Trabalhar com colunas e paginações
    total1, total2, total3, total4 =st.columns(4)
#Metric apresentar indicadores rapidos
    with total1:
        st.metric("Total Vendido", value=int(total_vendas))
    with total2:
        st.metric("Media por Produto", value=f"{media_vendas:.1f}")
    with total3:
        st.metric("Mediana", value=int(mediana_vendas))
    with total4:
        st.metric("Valor Total", value=float(total_valor))

    st.markdown("---")

def Graficos():
    #Criar gráfico de barras, mostrando quantidade de produtos por loja
    fig_barras = px.bar(
        df_selecao, 
        x="Produto",
        y="Quantidade",
        color="ID Loja",
        barmode="group",
        title="Quantidade de Produtos Vendidos por Loja"
    )

    #Gráfico de linhas com total de vendas por loja
    fig_linhas = px.line(
        df_selecao.groupby('ID Loja').sum(numeric_only=True).reset_index(),
        x="ID Loja",
        y="Quantidade",
        title="Total Vendas por Loja"
    )

    fig_valor_total = px.bar(
        df_selecao,
        x='ID Loja',
        y="Valor Final",
        color="ID Loja",
        barmode="group",
        title="Total Vendas em R$"
    )

    graf1, graf2, graf3 = st.columns(3)

    with graf1:
        st.plotly_chart(fig_barras, use_container_width=True)
    with graf2:
        st.plotly_chart(fig_linhas, use_container_width=True)
    with graf3:
        st.plotly_chart(fig_valor_total,use_container_width=True)

def sidebar():
    with st.sidebar:
        selecionado = option_menu(
            menu_title= "Menu",
            options=["Home","Gráficos"],
            icons=["house","bar-chart"],
            default_index=0
        )
    if selecionado == "Home":
        Home()
        Graficos()
    elif selecionado =="Gráficos":
        Graficos()

sidebar()

#python -m streamlit run projeto.py
