# Inicializa a lista para armazenar as temperaturas
#2- O Departamento Estadual de Meteorologia solicitou o desenvolvimento de um
#programa que armazene em um vetor um conjunto indeterminado de temperaturas, ao final
#informe a menor, a maior e a média das temperaturas.

temperaturas = []

while True:
    # Solicita a entrada do usuário
    temp_input = input("Digite uma temperatura (ou 'sair' para encerrar): ")
    
    if temp_input.lower() == 'sair':
        break  # Encerra o loop se o usuário digitar 'sair'
    
    try:
        # Converte a entrada para float e adiciona à lista
        temperatura = float(temp_input)
        temperaturas.append(temperatura)
    except ValueError:
        print("Por favor, digite um número válido ou 'sair'.")

# Verifica se foram inseridas temperaturas
if temperaturas:
    # Calcula a menor, a maior e a média das temperaturas
    menor_temp = min(temperaturas)
    maior_temp = max(temperaturas)
    media_temp = sum(temperaturas) / len(temperaturas)

    # Mostra os resultados
    print(f"\nMenor temperatura: {menor_temp:.2f}°C")
    print(f"Maior temperatura: {maior_temp:.2f}°C")
    print(f"Média das temperaturas: {media_temp:.2f}°C")
else:
    print("Nenhuma temperatura foi registrada.")
