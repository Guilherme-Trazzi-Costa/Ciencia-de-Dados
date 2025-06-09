# python -m streamlit run dashboard.py

# Comando para rodar o arquivo: python -m streamlit run dashboard.py

# Imports
import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

# Configuração da página
st.set_page_config(page_title='Dashboard Emissão de Carbono - Transportes!', page_icon='🚚', layout='wide')

def formatar_compacto(valor):
    if valor >= 1_000_000_000:
        return f'{valor / 1_000_000_000:.2f}B'
    elif valor >= 1_000_000:
        return f'{valor / 1_000_000:.2f}M'
    elif valor >= 1_000:
        return f'{valor / 1_000:.2f}K'
    else:
        return f'{valor:.2f}'


# Leitura das bases de dados
df_transportes = pd.read_excel('base_transportes.xlsx')
df_unificado = pd.read_excel('base_transportes_leve.xlsx')

# Filtros disponíveis na barra lateral
st.sidebar.header('Selecione os filtros')

# Filtro por Meio de Transporte
filtro_meio_transporte = st.sidebar.multiselect(
    "Meio de Transporte", 
    options = df_transportes['Meio de Transporte'].unique(),
    default = df_transportes['Meio de Transporte'].unique(),
    key="filtro_meio_transporte"
)

# Filtro por Combustível
filtro_combustivel = st.sidebar.multiselect(
    "Combustível", 
    options = df_transportes['Combustivel'].unique(),
    default = df_transportes['Combustivel'].unique(),
    key="filtro_combustivel"
)

# Filtro por Tipo de Transporte
filtro_tipo_transporte = st.sidebar.multiselect(
    "Tipo de Transporte", 
    options = df_transportes['Tipo de Transporte'].unique(),
    default = df_transportes['Tipo de Transporte'].unique(),
    key="filtro_tipo_transporte"
)

# Filtro por Atividade
filtro_atividade = st.sidebar.multiselect(
    "Atividade", 
    options = df_transportes['Atividade'].unique(),
    default = df_transportes['Atividade'].unique(),
    key="filtro_atividade"
)

# Filtro por Estado
filtro_estado = st.sidebar.multiselect(
    "Estado", 
    options = df_transportes['Estado'].unique(),
    default = df_transportes['Estado'].unique(),
    key="filtro_estado"
)

# Filtrando os dados com base nos filtros selecionados
df_filtrado = df_transportes.query(
    "`Meio de Transporte` in @filtro_meio_transporte and Combustivel in @filtro_combustivel and `Tipo de Transporte` in @filtro_tipo_transporte and Atividade in @filtro_atividade and Estado in @filtro_estado"
)

# Função para gerar os gráficos e métricas
def gerar_graficos():
    # Título da análise
    st.title('🚢 Análise Comparativa das Emissões de GEE nos Transportes de Carga Rodoviário, Ferroviário e Aquaviário no Brasil')

    # Definição das colunas de anos e fator de crédito de carbono
    colunas_anos = [2020, 2021, 2022, 2023]
    fator_credito_carbono = 0.05

    # Cálculo do total de emissões e créditos de carbono
    df_filtrado['Total Emissao'] = df_filtrado[colunas_anos].sum(axis=1)
    df_filtrado["Credito de Carbono"] = df_filtrado['Total Emissao'] * fator_credito_carbono
    porcentagem_credito = fator_credito_carbono * 100
    
    total_emissao = df_filtrado['Total Emissao'].sum()
    media_emissao = df_filtrado['Total Emissao'].mean()
    total_credito = df_filtrado['Credito de Carbono'].sum()

    # Exibindo as métricas
    metrica1, metrica2= st.columns(2)
    with metrica1:
        st.metric('Total de Emissão de Carbono (em Toneladas)', value=formatar_compacto(total_emissao))
    with metrica2:
        st.metric('Média de Emissão de Carbono (em Toneladas)', value=formatar_compacto(media_emissao))
    
    metrica3, metrica4 = st.columns(2)
    with metrica3:
        st.metric('Total de Crédito de Carbono (em Toneladas)', value=formatar_compacto(total_credito))
    with metrica4:
        st.metric('Porcentagem de Crédito de Carbono', value=f'{int(porcentagem_credito)}%')

    # Gráfico 1 - Emissões de CO2e por ano e meio de transporte
    df_co2 = df_unificado[df_unificado['Gás'] == 'CO2e (t) GWP-AR6']
    emissao_total_ano = px.line(
        df_co2.groupby(['Ano', 'Meio de Transporte'])['Emissão Total'].sum().reset_index(),
        x='Ano',
        y='Emissão Total',
        color='Meio de Transporte',
        title='Emissões Anuais de CO2e(t) GWP-AR6 de 2000 a 2023',
        labels = {'Emissão Total': 'CO2e (t) GWP-AR6'}
    )
    emissao_total_ano.update_layout(
        title_font=dict(size=18),
        xaxis_title_font=dict(size=16),
        yaxis_title_font=dict(size=16),
        legend_title_font=dict(size=16),
        legend_font=dict(size=16),
        font=dict(size=16),
        xaxis=dict(tickfont=dict(size=22)),
        yaxis=dict(tickfont=dict(size=22))
    )

    # Gráfico 2 - Emissões de GEE por gás e meio de transporte
    emissao_gas_group = df_filtrado.groupby(['Gás', 'Meio de Transporte'], as_index=False)[colunas_anos].sum()
    emissao_gas_group['Total Emissao'] = emissao_gas_group[colunas_anos].sum(axis=1)
    top_10_gas = emissao_gas_group.nlargest(10, 'Total Emissao')

    emissao_gas_10 = px.bar(
        top_10_gas,
        x="Gás",
        y='Total Emissao',
        color="Meio de Transporte",
        barmode="group",
        height=550,
        title="Emissões de Gases pelos Modais de Transporte de 2000 a 2023"
    )
    emissao_gas_10.update_layout(
        title_font=dict(size=18),
        xaxis_title_font=dict(size=16),
        yaxis_title_font=dict(size=16),
        legend_title_font=dict(size=16),
        legend_font=dict(size=16),
        font=dict(size=16),
        xaxis=dict(tickfont=dict(size=22)),
        yaxis=dict(tickfont=dict(size=22))
    )

    # Gráfico 3 - Emissão por tipo de combustível
    df_combustivel = df_transportes.groupby(['Combustivel']).size().reset_index(name='Quantidade')
    df_combustivel['Quantidade'] = pd.to_numeric(df_combustivel['Quantidade'], errors='coerce').astype('Int64')
    df_combustivel.loc[df_combustivel['Quantidade'] < 300, 'Combustivel'] = 'Outros'

    graf_combustivel = px.pie(
        df_combustivel,
        names="Combustivel",
        values="Quantidade",
        title="Quantidade utilizada de cada Combustível de 2000 a 2023",
        color="Combustivel",
        labels={"Quantidade": "Total de Ocorrências", "Produto ou sistema": "Combustível"},
        hole=0.5
    )
    graf_combustivel.update_traces(textinfo='percent', textfont_size=20)
    graf_combustivel.update_layout(
        title_font=dict(size=18),
        font=dict(size=16),
        height=550,
        legend_title_font=dict(size=16),
        legend_font=dict(size=16),
    )

    # Gráfico 4 - Emissão por estado de 2020 a 2023
    emissao_estado_group = df_filtrado.groupby("Estado", as_index=False)[colunas_anos].sum()
    emissao_estado_group['Total Emissao'] = emissao_estado_group[colunas_anos].sum(axis=1)
    top_5_estados = emissao_estado_group.nlargest(5, 'Total Emissao')

    emissao_estado_5 = px.bar(
        top_5_estados,
        x="Estado",
        y='Total Emissao',
        color="Estado",
        barmode="group",
        height=600,
        title="Estados com mais Emissões de Carbono de 2020 a 2023"
    )
    emissao_estado_5.update_layout(
        title_font=dict(size=18),
        xaxis_title_font=dict(size=16),
        yaxis_title_font=dict(size=16),
        legend_title_font=dict(size=16),
        legend_font=dict(size=16),
        font=dict(size=16),
        xaxis=dict(tickfont=dict(size=22)),
        yaxis=dict(tickfont=dict(size=22))
    )

    # Gráfico 5 - Comparação das emissões por meio de transporte ao longo dos anos
    df_agrupado = df_filtrado[df_filtrado['Gás'] == 'CO2e (t) GWP-AR6']
    df_agrupado = df_transportes.groupby('Meio de Transporte', as_index=False)[[2020, 2021, 2022, 2023]].sum()
    df_agrupado.columns = df_agrupado.columns.astype(str)

    df_long = df_agrupado.melt(id_vars='Meio de Transporte', var_name='Ano', value_name='Total Emissao')

    comparacao_transportes = px.bar(
        df_long, 
                x='Ano', 
                y='Total Emissao', 
                color='Meio de Transporte', 
                barmode='group',
                height=600,
                title='Emissões Anuais de cada Modal de Transporte de 2020 a 2023')
    comparacao_transportes.update_layout(
        title_font=dict(size=18),
        xaxis_title_font=dict(size=16),
        yaxis_title_font=dict(size=16),
        legend_title_font=dict(size=16),
        legend_font=dict(size=16),
        font=dict(size=16),
        xaxis=dict(tickfont=dict(size=22)),
        yaxis=dict(tickfont=dict(size=22))
    )

    # Exibindo os gráficos
    st.plotly_chart(emissao_total_ano, use_container_width=True)

    grafic1, grafic2 = st.columns(2)
    with grafic1:
        st.plotly_chart(emissao_gas_10, use_container_width=True)
    with grafic2:
        st.plotly_chart(graf_combustivel, use_container_width=True)

    graf1, graf2 = st.columns(2)
    with graf1:
        st.plotly_chart(emissao_estado_5, use_container_width=True)
    with graf2:
        st.plotly_chart(comparacao_transportes, use_container_width=True)

# Chamando a função para gerar os gráficos
gerar_graficos()