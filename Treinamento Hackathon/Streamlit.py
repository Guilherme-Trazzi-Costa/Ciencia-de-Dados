import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

#python -m streamlit run Streamlit.py



# Configuração da página
st.set_page_config(page_title="Dashboard Despesas", layout="wide")

# Carregando os dados
df = pd.read_excel("Orcamento_Tratado.xlsx")
df["Valor"] = df["Valor"].astype("float").replace(",", "X").replace(".", ",").replace("X", ".")

# Filtros
st.sidebar.header("Selecione os filtros")

setores = st.sidebar.multiselect(
    "Setores",
    options=df["Setor"].unique(),
    default=df["Setor"].unique(),
    key="setores"
)

tipos = st.sidebar.multiselect(
    "Tipos de Despesas",
    options=df["Tipo"].unique(),
    default=df["Tipo"].unique(),
    key="tipos"
)

fornecedores = st.sidebar.multiselect(
    "Fornecedores",
    options=df["Fornecedor"].unique(),
    default=df["Fornecedor"].unique(),
    key="fornecedores"
)

datas = st.sidebar.multiselect(
    "Datas",
    options=sorted(df["Data"].astype(str).unique()),
    default=sorted(df["Data"].astype(str).unique()),
    key="datas"
)

# Convertendo a coluna Data para string para permitir comparação com filtro
df["Data"] = df["Data"].astype(str)

# Aplicando os filtros
df_selecao = df.query(
    "Setor in @setores and Tipo in @tipos and Fornecedor in @fornecedores and Data in @datas"
)


# Funções de páginas
def Home(df_filtrado):
    st.title("Análise de Despesas")

    total_despesas = df_filtrado["Valor"].sum()
    media_despesas = df_filtrado["Valor"].mean()
    

    

    total1, total2, = st.columns(2)
    with total1:
        total1.metric("Total de Despesas", value=f"R$ {total_despesas:,.2f}")
    with total2:
        total2.metric("Media de Despesas", value= f"R$ {media_despesas:,.2f}")
    st.markdown("---")
    

def Graficos(df_filtrado):
    st.subheader("Gráfico de Despesas por Setor")

    #media_por_data = df_filtrado.groupby("Data", as_index=False)["Valor"].mean()
    tipo_despesa = df_filtrado.groupby("Tipo", as_index=False)["Valor"].sum()
    salario_df = df_filtrado[df_filtrado["Tipo"] == "Salário"]


    salario_area = salario_df.groupby("Setor", as_index=False)["Valor"].sum()

    #media_por_data = df.groupby("Data")["Valor"].mean()

    

    despesas_setor = px.bar(
        df_filtrado,
        x="Setor",
        y="Valor",
        color="Setor",
        barmode="group",
        title="Despesas por Setor"
    )

    despesa = px.bar(
        tipo_despesa,
            x="Tipo",
            y="Valor",
            color="Tipo",
            barmode="group",
            title="Tipo de Gasto"
    )

    


    salario_por_area = px.bar(
        salario_area,
            x="Setor",
            y="Valor",
            color="Setor",
            barmode="group",
            title="Salario por Área"
    )

    

    graf1, graf2, graf3, graf4 = st.columns(4)

    with graf1:
        st.plotly_chart(despesas_setor, use_container_width=True)
    with graf2:
        st.plotly_chart(despesa, use_container_width=True)
    with graf3:
        st.plotly_chart(salario_por_area, use_container_width=True)



# Menu lateral
def sidebar():
    with st.sidebar:
        selecionado = option_menu(
            menu_title="Menu",
            options=["Home", "Gráficos"],
            icons=["house", "bar-chart"],
            default_index=0
        )

    # Páginas
    if selecionado == "Home":
        Home(df_selecao)
        Graficos(df_selecao)
    elif selecionado == "Gráficos":
        Graficos(df_selecao)

# Executa o menu
sidebar()

# Agrupar por Fornecedor e Tipo, somando os valores
valor_fornecedores = df_selecao.groupby(["Fornecedor", "Tipo"], as_index=False)["Valor"].sum()

# Selecionar os 5 maiores valores
top_5 = valor_fornecedores.nlargest(5, "Valor", keep="all")

# Exibir no Streamlit
exib = st.columns(1)[0]
with exib:
    st.write("Top 5 Fornecedores por Tipo")
    st.dataframe(top_5, hide_index=True)