import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from query import conexao

#python -m streamlit run dash_integrador.py
query = "SELECT * FROM tb_litoral"

df = conexao(query)

if st.button("Atualizar Dados"):
    df = conexao(query)


localizacao = st.sidebar.multiselect("Localizacao Selecionada",
                                     options=df["localizacao"].unique(),
                                     default=df["localizacao"].unique()
                                     )

# dia = st.sidebar.multiselect("Dia Selecionado",
#                              options = df["dia"].unique(),
#                              default = df["dia"].unique()
#                              )

# periodo = st.sidebar.multiselect("Periodo Selecionado",
#                                 options = df["periodo"].unique(),
#                                 default = df["periodo"].unique()
# )

dia_hora = st.sidebar.multiselect("Dia Selecionado",
                             options = df["dia_hora"].unique(),
                             default = df["dia_hora"].unique()
                             )

min_co2 = float(df["co2"].min())

max_co2 = float(df["co2"].max())

co2 = st.sidebar.slider(
    "Intervalo Nível de CO2 Selecionado",
    min_value=min_co2,
    max_value=max_co2,
    value=(min_co2, max_co2) 
    )

#------------------POEIRA NÃO FOI COLETADA----------------------
# min_poeira_1 = float(df["poeira_1"].min())

# max_poeira_1 = float(df["poeira_1"].max())

# poeira_1 = st.sidebar.slider(
#     "Intervalo Nível de Poeira_1 Selecionada",
#     min_value=min_poeira_1,
#     max_value=max_poeira_1,
#     value=(min_poeira_1, max_poeira_1) 
#     )

# min_poeira_2 = float(df["poeira_2"].min())

# max_poeira_2 = float(df["poeira_2"].max())

# poeira_2 = st.sidebar.slider(
#     "Intervalo Nível de Poeira_2 Selecionada",
#     min_value=min_poeira_2,
#     max_value=max_poeira_2,
#     value=(min_poeira_2, max_poeira_2) 
#     )

#--------------------------------------------------------

min_pressao = float(df["pressao"].min())

max_pressao = float(df["pressao"].max())

pressao = st.sidebar.slider(
    "Intervalo Nível de Pressão Selecionada",
    min_value=min_pressao,
    max_value=max_pressao,
    value=(min_pressao, max_pressao)
    )

min_umidade = float(df["umidade"].min())

max_umidade = float(df["umidade"].max())

umidade = st.sidebar.slider(
    "Intervalo Nível de Umidade Selecionada",
    min_value=min_umidade,
    max_value=max_umidade,
    value=(min_umidade, max_umidade)
    )

min_temperatura = float(df["temperatura"].min())

max_temperatura = float(df["temperatura"].max())

temperatura = st.sidebar.slider(
    "Intervalo de Temperatura Selecionada",
    min_value=min_temperatura,
    max_value=max_temperatura,
    value=(min_temperatura, max_temperatura) 
    )

min_altitude = float(df["altitude"].min())

max_altitude = float(df["altitude"].max())

altitude = st.sidebar.slider(
    "Intervalo de Altitude Selecionada",
    min_value=min_altitude,
    max_value=max_altitude,
    value=(min_altitude, max_altitude) 
    )

#---------------COLUNAS TABELA 2-------------------------------
# min_qualidade_ar = float(df["qualidade_ar"].min())

# max_qualidade_ar = float(df["qualidade_ar"].max())

# qualidade_ar = st.sidebar.slider(
#     "Intervalo de Nível Qualidade do Ar Selecionada",
#     min_value=min_qualidade_ar,
#     max_value=max_qualidade_ar,
#     value=(min_qualidade_ar, max_qualidade_ar) 
#     )

# min_densidade_ar = float(df["densidade_ar"].min())

# max_densidade_ar = float(df["densidade_ar"].max())

# densidade_ar = st.sidebar.slider(
#     "Intervalo de Nível Densidade do Ar Selecionada",
#     min_value=min_densidade_ar,
#     max_value=max_densidade_ar,
#     value=(min_densidade_ar, max_densidade_ar) 
#     )

# min_velocidade_vento = float(df["velocidade_vento"].min())

# max_velocidade_vento = float(df["velocidade_vento"].max())

# velocidade_vento = st.sidebar.slider(
#     "Intervalo de Velocidade Vento Selecionada",
#     min_value=min_velocidade_vento,
#     max_value=max_velocidade_vento,
#     value=(min_velocidade_vento, max_velocidade_vento)
#     )

# min_previsao_chuva = float(df["previsao_chuva"].min())

# max_previsao_chuva = float(df["previsao_chuva"].max())

# previsao_chuva = st.sidebar.slider(
#     "Intervalo de Previsão de Chuva Selecionada",
#     min_value=min_previsao_chuva,
#     max_value=max_previsao_chuva,
#     value=(min_previsao_chuva, max_previsao_chuva) 
#     )

#---------------------------------------------------------------------------


df_selecionado = df[
    (df["localizacao"].isin(localizacao)) &
    (df["dia_hora"].isin(dia_hora)) &
    # (df["periodo"].isin(periodo)) &
    (df["co2"] >= co2[0]) &
    (df["co2"] <= co2[1]) &
    # (df["poeira_1"] >= poeira_1[0]) &
    # (df["poeira_1"] <= poeira_1[1]) &
    # (df["poeira_2"] >= poeira_2[0]) &
    # (df["poeira_2"] <= poeira_2[1]) &
    (df["pressao"] >= pressao[0]) &
    (df["pressao"] <= pressao[1]) &
    (df["umidade"] >= umidade[0]) &
    (df["umidade"] <= umidade[1]) &
    (df["temperatura"] >= temperatura[0]) &
    (df["temperatura"] <= temperatura[1]) &
    (df["altitude"] >= altitude[0]) &
    (df["altitude"] <= altitude[1]) 
    # (df["qualidade_ar"] >= qualidade_ar[0]) &
    # (df["qualidade_ar"] <= qualidade_ar[1]) &
    # (df["densidade_ar"] >= densidade_ar[0]) &
    # (df["densidade_ar"] <= densidade_ar[1]) &
    # (df["velocidade_vento"] >= velocidade_vento[0]) &
    # (df["velocidade_vento"] <= velocidade_vento[1]) &
    # (df["previsao_chuva"] >= previsao_chuva[0]) &
    # (df["previsao_chuva"] <= previsao_chuva[1])
                  
]



