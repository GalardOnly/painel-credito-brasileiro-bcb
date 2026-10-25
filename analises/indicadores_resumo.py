import pandas as pd

# Coleta os valores necessários usando iloc
s_inicio = df.iloc[0]['saldo_milhoes']
s_fim = df.iloc[-1]['saldo_milhoes']
t_fim = df.iloc[-1]['taxa_pct']

# Cria o dicionário com a estrutura exata pedida
dados = {
    'indicador': ['saldo_inicio', 'saldo_fim', 'taxa_fim'],
    'valor': [s_inicio, s_fim, t_fim]
}

# Define o DataFrame final na variável esperada
resultado = pd.DataFrame(dados)
