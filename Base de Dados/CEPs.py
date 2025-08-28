import pandas as pd

df = pd.read_excel('Base_Limpa_Brasil.xlsx')
df2 = pd.read_excel('CEP_dos_municipios.xlsx')

# Divide intervalo de CEPs
novo = df2['CEP'].str.split(' à ', n=1, expand=True)
df2['CEP1'] = novo[0]
df2['CEP2'] = novo[1]

# Remove linhas com nome "Nan"
indiceDelet = df[df['Nome'] == 'Nan'].index
df = df.drop(index=indiceDelet)

# Remove hífens dos CEPs
df['CEP'] = df['CEP'].str.replace('-', '', regex=False)
df2['CEP1'] = df2['CEP1'].str.replace('-', '', regex=False)
df2['CEP2'] = df2['CEP2'].str.replace('-', '', regex=False)

# Converte para inteiro
df['CEP'] = df['CEP'].astype(int)
df2['CEP1'] = df2['CEP1'].astype(int)
df2['CEP2'] = df2['CEP2'].astype(int)

# Função para encontrar o município com base no CEP
def encontrarCEP(cep):
    for _, linha in df2.iterrows():
        if linha['CEP1'] <= cep <= linha['CEP2']:
            return linha['Município']
    return None

# Aplica a função
df['Municipio'] = df['CEP'].apply(encontrarCEP)

# Mostra resultado
print(df[['CEP', 'Municipio']])

df.to_excel("Teste CEPs.xlsx")
