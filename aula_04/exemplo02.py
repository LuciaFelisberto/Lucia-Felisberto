#informar ao usuário qye nao sera possivel dividir o numero inteiro por zero
#nao é possivel dividir por zero( inofrmar ao usuario)
n1 = int(input("informe o primeira valor: "))
n2 = int(input("informe o segunda valor: "))
try:
    result = n1 / n2
except ZeroDivisionError:
    print("nao é possivel dividir por zero.")
else:
    print(result)