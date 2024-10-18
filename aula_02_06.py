import pandas as pd

# Vendas dos últimos 7 dias
vendas = {
    "Maria": [800, 700, 1000, 900, 1200, 600, 600],
    "João": [900, 500, 1100, 1000, 900, 500, 700],
    "Manuel": [700, 600, 900, 1200, 900, 700, 400]
}

# Criar um DataFrame a partir do dicionário de vendas
df_vendas = pd.DataFrame(vendas)

# Calcular média, maior e menor venda
resultados = {
    "Média": df_vendas.mean(),
    "Maior": df_vendas.max(),
    "Menor": df_vendas.min()
}

# Criar um DataFrame para os resultados
df_resultados = pd.DataFrame(resultados)

# Transpor o DataFrame para melhor visualização
df_resultados = df_resultados.T

# Apresentação dos resultados
print("Resultados das vendas dos últimos 7 dias:")
print(df_resultados)



