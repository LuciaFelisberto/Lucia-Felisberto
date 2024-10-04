try:
    n1 = int(input("informe o primeira valor: "))
    n2 = int(input("informe o segunda valor: "))
except ValueError:
    print ("verifique a entrada de dados")
else:
    try:
        result = n1 / n2
    except ZeroDivisionError:
    print("nao é possivel dividir por zero.")
    else:
    print(result)