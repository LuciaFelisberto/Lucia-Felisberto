#3- Foi realizada uma pesquisa de algumas características físicas da população de uma certa região, a

#qual coletaram os seguintes dados referentes a cada habitante para serem analisados:

#- sexo (masculino e feminino)
#- cor dos olhos (azuis, verdes ou castanhos)
#- cor dos cabelos (louros, castanhos, pretos)
#- idade
#Faça um programa que determine e escreva:
#a) a maior e a menor idade dos habitantes, assim como a média das idades;
#b) a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos, inclusive;
#c) a quantidade de indivíduos que tenham olhos verdes e cabelos louros;

# Inicializa as listas e contadores
idades = []
sexo_feminino = 0
olhos_verdes_cabelos_louros = 0

while True:
    # Coleta os dados do habitante
    sexo = input("Digite o sexo (M/F) ou 'sair' para encerrar: ").strip().lower()
    if sexo == 'sair':
        break
    
    cor_olhos = input("Digite a cor dos olhos (azuis, verdes, castanhos): ").strip().lower()
    cor_cabelos = input("Digite a cor dos cabelos (louros, castanhos, pretos): ").strip().lower()
    idade = int(input("Digite a idade: "))
    
    # Adiciona a idade à lista
    idades.append(idade)
    
    # Contagem de mulheres entre 18 e 35 anos
    if sexo == 'f' and 18 <= idade <= 35:
        sexo_feminino += 1
    
    # Contagem de indivíduos com olhos verdes e cabelos louros
    if cor_olhos == 'verdes' and cor_cabelos == 'louros':
        olhos_verdes_cabelos_louros += 1

# A) Análise das idades
if idades:
    maior_idade = max(idades)
    menor_idade = min(idades)
    media_idades = sum(idades) / len(idades)
    
    print(f"\nMaior idade: {maior_idade}")
    print(f"Menor idade: {menor_idade}")
    print(f"Média das idades: {media_idades:.2f}")
else:
    print("Nenhuma idade registrada.")

# B) Quantidade de indivíduos do sexo feminino entre 18 e 35 anos
print(f"Quantidade de mulheres entre 18 e 35 anos: {sexo_feminino}")

# C) Quantidade de indivíduos com olhos verdes e cabelos louros
print(f"Quantidade de indivíduos com olhos verdes e cabelos louros: {olhos_verdes_cabelos_louros}")
