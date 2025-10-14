import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu #para trabalhar com menu
from query import conexao

#********Primeira Consulta e Atualização******************

#python -m streamlit run projeto.py


#Consulta SQL
query = "SELECT * FROM tb_carro"

#Carregar dados para variável df
df = conexao(query)

#Atualização - Botão
if st.button("Atualizar Dados"):
    df = conexao(query)

#*********************************************

#Estrutura Filro Lateral
#sidebar = barra lateral
marca =st.sidebar.multiselect("Marca Selecionada",
                       options=df["marca"].unique(), #Escrito no banco
                       default=df["marca"].unique()
                       )

modelo = st.sidebar.multiselect("Modelo Selecionado",
                       options=df["modelo"].unique(), #Escrito no banco
                       default=df["modelo"].unique()
                       )

ano = st.sidebar.multiselect("Ano Selecionado",
                       options=df["ano"].unique(), #Escrito no banco
                       default=df["ano"].unique()
                       )

cor = st.sidebar.multiselect("Cor Selecionada",
                       options=df["cor"].unique(), #Escrito no banco
                       default=df["cor"].unique()
                       )


min_valor = int(df["valor"].min())

max_valor = int(df["valor"].max())

valor = st.sidebar.slider(
    "Intervalo Valor Selecionado",
    min_value=min_valor,
    max_value=max_valor,
    value=(min_valor, max_valor) #Valor Inicial
    )



min_vendas = int(df["numero_vendas"].min())

max_vendas = int(df["numero_vendas"].max())

vendas = st.sidebar.slider(
    "Intervalo Número de Vendas Selecionado",
    min_value=min_vendas,
    max_value=max_vendas,
    value=(min_vendas, max_vendas) #Valor Inicial
    )

#*********************Verificação Aplicação Filtros********************
df_selecionado = df[
    (df["marca"].isin(marca)) &
    (df["modelo"].isin(modelo)) &
    (df["ano"].isin(ano)) &
    (df["cor"].isin(cor)) &
    (df["valor"] >= valor[0]) &
    (df["valor"] <= valor[1]) &
    (df["numero_vendas"] >= vendas[0]) & #0 para valor minimo
    (df["numero_vendas"] <= vendas[1]) #1 para valor maximo
]


#**************************DASHBOARD*****************************

#CARDS DE VALORES
def pagina_inicial():
    #Expande para selecionar as opções
    with st.expander("Tabela de Carros"):
        exibicao = st.multiselect("Filtro", 
                                  df_selecionado.columns,
                                  default=[],
                                  key = "Filtro_Exibicao"
                                )
        
        if exibicao:
            st.write(df_selecionado[exibicao])

    if not df_selecionado.empty:
        total_vendas = df_selecionado["numero_vendas"].sum()
        media_valor = df_selecionado["valor"].mean()
        media_vendas = df_selecionado["numero_vendas"].mean()

        card1, card2, card3 = st.columns(3, gap="large")
        with card1:
            st.info("Valor Total de Vendas")
            st.metric(label="Total", value=f"{total_vendas:,.0f}")

        with card2:
            st.info("Valor Médio de Carros")
            st.metric(label="Média", value=f"{media_valor:,.0f}")

        with card3:
            st.info("Valor Médio de Vendas")
            st.metric(label="Média", value=f"{media_vendas:,.0f}")

    else:
        st.warning("Nenhum dado disponível com os filtros selecionados")
    st.markdown("""------""")

#*********************************Gráfcios********************************************************

def graficos(df_selecionado):
    if df_selecionado.empty:
        st.warning("Nenhum dado disponivel para gerar gráficos")
        return
    
    graf1, graf2= st.tabs(["Gráfico Barras",
                                          "Gráfico Linhas"
                                          ])
    
    with graf1:
        st.write("Gráfico Barras")
        valor = df_selecionado.groupby("marca").count()[["valor"]].sort_values(by="valor", ascending=False)

        fig1 = px.bar(
            valor,
            x = valor.index, #Marcas
            y = "valor",
            orientation="v",
            title = "Valores dos Carros por Marca",
            color_discrete_sequence= ["#0083b8"] # Cor sempre em hexadecimal
        )

        st.plotly_chart(fig1, use_container_width = True)

    with graf2:
        st.write("Gráfico Linhas")
        valor_linhas = df_selecionado.groupby("modelo").count()[["valor"]]


        fig2 = px.line(
            valor_linhas,
            x = valor_linhas.index,
            y = "valor",
            title = "Valor por Modelo",
            color_discrete_sequence=["#e70f0f"]

        )

        st.plotly_chart(fig2, use_container_width = True)

    










pagina_inicial()
graficos(df_selecionado)

                                  