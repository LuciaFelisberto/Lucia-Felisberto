
maior = 0
soma_F = 0
soma_M = 0
cont_F = 0
cont_M = 0
for i in range(5):
    nome = input("informe o nome: ")
    sexo = input("informe o sexo: ")
    idade = int(input("informe a idade:"))
    if idade > maior:
        maior = idade
        soma = soma + idade
    if sexo == "M" or sexo == "m":
        soma_M = soma_M + idade
        cont_M += 1
    if sexo == "F" or sexo == "f":
        soma_F = soma_F + idade
        cont_F += 1
media_M = soma_M / cont_M
media_F = soma_F / cont_F
print(f"a soma da idade dos homens é {soma_M}")
print(f"a soma da idade das mulheres é {soma_F}")
print(f"a média da idade dos homens é{media_M: .0f}")
print(f"a soma da idade das mulheres é {media_F: .0f}")
print(f"a maior idade é {maior}")