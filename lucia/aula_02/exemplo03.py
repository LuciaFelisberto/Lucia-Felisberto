#valor final da prestaçao
prestacao = float(input("informe o valor da prestacão:"))
taxa = float(input("informe a taxa de juros mensal: "))
tempo = int(input("informe a quantidade de meses em atraso: "))
valor_final  = prestacao+(prestacao*taxa/100*tempo)
print(f"o valor em atraso era de r$ {valor_final: .2f}")