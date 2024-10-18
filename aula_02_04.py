# Dados fornecidos
populacao_vacinada = [30000000, 25000000, 10000000, 5000000]
populacao_total = [213317639, 214477744, 215574303, 216687971]

# Cálculo do total e da média de pessoas vacinadas
total_vacinados = sum(populacao_vacinada)
media_vacinados = total_vacinados / len(populacao_vacinada)

# Cálculo do total e da média da população
total_populacao = sum(populacao_total)
media_populacao = total_populacao / len(populacao_total)

# Cálculo da taxa de vacinação anual
taxas_vacinacao = [(vacinados / total) * 100 for vacinados, total in zip(populacao_vacinada, populacao_total)]

# Apresentação dos resultados
print(f"Total de pessoas vacinadas: {total_vacinados}")
print(f"Média de pessoas vacinadas: {media_vacinados:.2f}")
print(f"Total da população do Brasil: {total_populacao}")
print(f"Média da população do Brasil: {media_populacao:.2f}")
print("Taxas de vacinação anual dos últimos 4 anos:")
for ano, taxa in enumerate(taxas_vacinacao, start=1):
    print(f"Ano {ano}: {taxa:.2f}%")

