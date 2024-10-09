#1- Faça um programa que pergunte quanto um funcionário recebe por hora e o número de
#horas trabalhadas no mês. Calcule e mostre o total do seu salário, sabendo que são descontados 11%
#para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

#a) salário bruto.
#b) quanto pagou ao IRRF.
#c) quanto pagou ao INSS.
#d) quanto pagou ao sindicato.
#e) o salário líquido.

# Solicita o valor recebido por hora e o número de horas trabalhadas no mês
valor_por_hora = float(input("Digite quanto você recebe por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

# Calcula o salário bruto
salario_bruto = valor_por_hora * horas_trabalhadas

# Calcula os descontos
irrf = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

# Calcula o salário líquido
salario_liquido = salario_bruto - (irrf + inss + sindicato)

# Mostra os resultados
print(f"\nSalário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto do IRRF: R$ {irrf:.2f}")
print(f"Desconto do INSS: R$ {inss:.2f}")
print(f"Desconto do Sindicato: R$ {sindicato:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
