# python -m streamlit run dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Dashboard Emissão de Carbono - Transportes!', page_icon='🚚', layout='wide')

df = pd.read_excel('base_transportes.xlsx')

df_unificado = pd.read_excel('base_transportes_leve.xlsx')
#Filtros

st.sidebar.header('Selecione os filtros')

#Filtro por Meio de Transporte
meio_transporte = st.sidebar.multiselect(
#Opções filtro
    "Meio de Transporte", 
    options = df['Meio de Transporte'].unique(),
#Opção que vem por padrão no filtro
    default = df['Meio de Transporte'].unique(),
#Chave única
    key="meio_transporte"
)

#Filtro por combustivel
combustivel = st.sidebar.multiselect(
#Opções filtro
    "Combustivel", 
    options = df['Combustivel'].unique(),
#Opção que vem por padrão no filtro
    default = df['Combustivel'].unique(),
#Chave única
    key="combustivel"
)

#Filtro por Tipo de Transporte
tipo_transporte = st.sidebar.multiselect(
#Opções filtro
    "Tipo de Transporte", 
    options = df['Tipo de Transporte'].unique(),
#Opção que vem por padrão no filtro
    default = df['Tipo de Transporte'].unique(),
#Chave única
    key="tipo_transporte"
)

#Filtro por Atividade
atividade = st.sidebar.multiselect(
#Opções filtro
    "Atividade", 
    options = df['Atividade'].unique(),
#Opção que vem por padrão no filtro
    default = df['Atividade'].unique(),
#Chave única
    key="atividade"
)

#Filtro por Estado
estado = st.sidebar.multiselect(
#Opções filtro
    "Estado", 
    options = df['Estado'].unique(),
#Opção que vem por padrão no filtro
    default = df['Estado'].unique(),
#Chave única
    key="estado"
)


# Menu

with st.sidebar:
        selecionado = option_menu(
            menu_title='Menu',
            options=['Gráficos'],
            default_index=0
        )

df_filtrado = df.query(
    "`Meio de Transporte` in @meio_transporte and Combustivel in @combustivel and `Tipo de Transporte` in @tipo_transporte and Atividade in @atividade and Estado in @estado"
)
# Metricas

def graficos():

    st.title('🚢 Análise Comparativa das Emissões de GEE nos Transporte de Carga Rodoviário, Ferroviário e Aquaviário no Brasil')
    colunas_anos = [2020, 2021, 2022, 2023] 

    fator_crédito = 0.05

    df_filtrado['Total'] = df_filtrado[colunas_anos].sum(axis=1)

    df_filtrado["Crédito de Carbono"] = df_filtrado['Total']*fator_crédito

    porcentagem_créditos = fator_crédito*100
    
    total_emissao = df_filtrado['Total'].sum()
    media_emissao = df_filtrado['Total'].mean()
    total_credito = df_filtrado['Crédito de Carbono'].sum()

    metrica1, metrica2, metrica3, metrica4 = st.columns(4)
    with metrica1:
         st.metric('Total de Emissão de Crabono', value=f'{total_emissao:.2f}')
    with metrica2:
         st.metric('Média de Emissão de carbono', value=f'{media_emissao:.2f}')
    with metrica3:
         st.metric('Total de Crédito de Crabono', value=f'{total_credito:.2f}')
    with metrica4:
         st.metric('Porcentagem de Crédito de Crabono', value=f'{porcentagem_créditos:.2f}%')
    

#Gráficos

    # graf1
    # st.title('Comparação das Emissões de GEE nos Transporte de Carga Rodoviário, Ferroviário e Aquaviário no Brasil')
    # #df_gas = df_filtrado[df_filtrado['Meio de Transporte'].isin(['Hidroviário', 'Ferroviário', 'Rodoviário'])]
    # ordem_modais = ['Hidroviário', 'Ferroviário', 'Rodoviário']
    # df_filtrado['Meio de Transporte'] = pd.Categorical(df_filtrado['Meio de Transporte'], categories=ordem_modais, ordered=True)

    # # Somar emissões por gás para todos os modais
    # total_por_gas = df_filtrado.groupby('Gás')[colunas_anos].sum()
    # # Selecionar os 9 maiores gases
    # gases_maiores = total_por_gas.nlargest(9,total_por_gas)
    # df_filtrado = df_filtrado[df_filtrado['Gás'].isin(gases_maiores)]

    # # Agrupar dados por gás e modal
    # df_agrupado = (
    #     df_filtrado.groupby(['Gás', 'Meio de Transporte'])[colunas_anos]
    #     .sum()
    #     .reset_index()
    # )

    # df_agrupado['Gás'] = pd.Categorical(df_agrupado['Gás'], categories=gases_maiores, ordered=True)
    # fig = px.bar(
    #     df_agrupado,
    #     x='Gás',
    #     y='2023',
    #     color='Meio de Transporte',
    #     barmode='group',
    #     category_orders={'Meio de Transporte': ordem_modais, 'Gás': gases_maiores},
    #     labels={
    #         '2023': 'Emissões (t)',
    #         'Meio de Transporte': 'Modal de Transporte',
    #         'Gás': 'Tipo de Gás'
    #     },
    # )

    # fig.update_traces(texttemplate='%{y:.4s}', textposition='outside')
    # fig.update_layout(
    #     uniformtext_minsize=8,
    #     uniformtext_mode='hide',
    #     xaxis_tickangle=-45,
    #     yaxis_title='Emissões (t)',
    #     legend_title_text='Modal de Transporte',
    #     margin=dict(t=80, b=150),
    #     height=600,
    # )

    # st.plotly_chart(fig, use_container_width=True)

    emissao_gas_group = df_filtrado.groupby(['Gás', 'Meio de Transporte'], as_index=False)[colunas_anos].sum()
    emissao_gas_group['Total'] = emissao_gas_group[colunas_anos].sum(axis=1)

    top_10_gas = emissao_gas_group.nlargest(10, 'Total')

        # Criando o gráfico de barras
    emissao_gas_10 = px.bar(
            top_10_gas,
            x="Gás",
            y='Total',
            color="Meio de Transporte",
            barmode="group",
            title="Top 5 Estados com mais emissão de 2020 à 2023"
        )
    emissao_gas_10.update_traces(texttemplate='%{y:.4s}', textposition='outside')
    emissao_gas_10.update_layout(
        uniformtext_minsize=8,
        uniformtext_mode='hide',
        xaxis_tickangle=-45,
        yaxis_title='Emissões (t)',
        legend_title_text='Modal de Transporte',
        margin=dict(t=80, b=150),
        height=600,
    )
    emissao_gas_10.update_traces(textposition='outside')
    emissao_gas_10.update_layout(height=550)


    #graf2
    

    df_co2 = df_unificado [df_unificado ['Gás'] == 'CO2e (t) GWP-AR6']

    emissao_total_ano = px.line(
        df_co2.groupby(['Ano', 'Meio de Transporte'])['Emissão Total'].sum().reset_index(),
        x='Ano',
        y='Emissão Total',
        color='Meio de Transporte',
        title='Emissão Total por Ano',
        labels = {
            'Emissão Total': 'CO2e (t) GWP-AR6'
        }
    )


    #graf3
#graf2 - Emissao por tipo de combustivel
    df_ = df.groupby(['Combustivel']).size().reset_index(name='Quantidade')
    
    df_['Quantidade'] = pd.to_numeric(df_['Quantidade'], errors='coerce').astype('Int64')

    df_.loc[df_['Quantidade'] < 300, 'Combustivel'] = 'Outros'

    # Gráfico de rosquinha
    graf_comb = px.pie(
        df_,
        names="Combustivel",
        values="Quantidade",
        title="Quantidade utilizada de cada Combustível nos anos de 2000 a 2023",
        color="Combustivel",
        labels={
            "Quantidade": "Total de ocorrências",
            "Produto ou sistema": "Combustível"
        },
        hole=0.5
    )

    graf_comb.update_traces(textinfo='percent', textfont_size=20)
    graf_comb.update_layout(height=550)


    #graf4
#Gráfico 4 - Emissão por estado de 2020 à 2023
    
    emissao_estado_group = df_filtrado.groupby("Estado", as_index=False)[colunas_anos].sum()
    emissao_estado_group['Total'] = emissao_estado_group[colunas_anos].sum(axis=1)

    top_5_estados = emissao_estado_group.nlargest(5, 'Total')

        # Criando o gráfico de barras
    emissao_estado_5 = px.bar(
            top_5_estados,
            x="Estado",
            y='Total',
            color="Estado",
            barmode="group",
            title="Top 5 Estados com mais emissão de 2020 à 2023"
        )
    emissao_estado_5.update_traces(textposition='outside')
    emissao_estado_5.update_layout(height=550)
    #graf5
    df_agrupado = df_filtrado [df_filtrado ['Gás'] == 'CO2e (t) GWP-AR6']
    df_agrupado = df.groupby('Meio de Transporte', as_index=False)[[2020, 2021, 2022, 2023]].sum()
    df_agrupado.columns = df_agrupado.columns.astype(str)

    df_long = df_agrupado.melt(id_vars='Meio de Transporte', 
                            var_name='Ano', 
                            value_name='Total de emissões')

    comparacao_transportes = px.bar(df_long, 
                x='Ano', 
                y='Total de emissões', 
                color='Meio de Transporte', 
                barmode='group',
                height=600,
                title='Emissões por Ano e Modal de Transporte')
    
    st.plotly_chart(emissao_total_ano, use_container_width=True)

    grafic1, grafic2 = st.columns(2)
    with grafic1:
        st.plotly_chart(emissao_gas_10, use_container_width=True)
    with grafic2:
        st.plotly_chart(graf_comb, use_container_width=True)
    
    graf1, graf2 = st.columns(2)
    with graf1:
        st.plotly_chart(emissao_estado_5, use_container_width=True)
    with graf2:
        st.plotly_chart(comparacao_transportes, use_container_width=True)
    
        

def side_bar():
    if selecionado == 'Gráficos':
        graficos()

side_bar()