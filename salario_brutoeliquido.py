import os
os.system ("cls")

#faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
#sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: 
#• salário bruto. 
#• quanto pagou ao INSS. 
#• quanto pagou ao sindicato. 
#• o salário líquido. 
#• calcule os descontos e o salário líquido, conforme a tabela abaixo: + Salário Bruto : R$ - IR (11%) : R$ - INSS (8%) : R$ - Sindicato ( 5%) : R$ = Salário Liquido : R$ 
#Salario bruto- salario liquido
#porcentagem (% / 100)

#Entrada
print("Calculadora de Salário Líquido")
salario_hora = float(input("Digite quanto você ganha por hora: R$ "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

#Processamento
salario_bruto = salario_hora * horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - sindicato

#Saída
print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto do IR (11%): R$ {ir:.2f}")
print(f"Desconto do INSS (8%): R$ {inss:.2f}")
print(f"Desconto do Sindicato (5%): R$ {sindicato:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
