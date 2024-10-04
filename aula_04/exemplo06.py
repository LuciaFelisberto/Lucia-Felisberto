#com desconto
#informe a quantidade adquirida pelo preço unitario, valor total
nome = input("arroz")
quant = int(input("a quantidade adquirida de arroz é: "))
valor = float(input("o preço unitario é: "))
except ValueError:
print("verifique os valores informados")
else:
total = valor * quant
print(f"o valor total sem desconto é R$: {total: .2f}")
if quant <= 5:
        desc = total * 0.98
elif quant > 5 and quant <= 10:
        desc = total * 0.97
else:
        desc = total * 0.95
print(f"o valor total com desconto é R$ {desc: .2f}")

