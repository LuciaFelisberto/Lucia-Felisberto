import pandas as pd

# Dados fornecidos
dados = {
    "Roubo": [100, 90, 80, 120, 110, 90, 70],
    "Furto": [80, 60, 70, 60, 100, 50, 30],
    "Recuperacao": [70, 50, 90, 80, 100, 70, 50]
}

# Criar um DataFrame a partir do dicionário
df = pd.DataFrame(dados)

# Calcular a quantidade total de roubos + furtos
df['Total'] = df['Roubo'] + df['Furto']

# Calcular a taxa de recuperação diária
df['Taxa Recuperacao'] = df['Recuperacao'] / df['Roubo'] * 100
df['Taxa Recuperacao'] = df['Taxa Recuperacao'].fillna(0)  # Preencher NaN com 0 caso haja divisão por zero

# Apresentação dos resultados
print("Resultados das estatísticas de roubos e furtos dos últimos 7 dias:")
print(df[['Roubo', 'Furto', 'Total', 'Recuperacao', 'Taxa Recuperacao']])























