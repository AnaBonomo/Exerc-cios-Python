import os
os.system ("cls")

#Problema: Desenvolva um programa que solicite o nome do funcionário e o salário atual.
#A empresa concederá:
#Salário até R$ 2.000,00: aumento de 10%;
#Salário até R$ 5.000,00: aumento de 7%;
#Salário acima de R$ 5.000,00: aumento de 5%.
#Apresente o salário atual, o percentual de aumento, o valor do aumento e o novo salário.

print ("Cálculo de aumento salarial")
nome = input("Digite o nome do funcionário: ")
salario_atual = float(input("Digite o salário atual: R$ "))

if salario_atual <= 2000:
    aumento = salario_atual * 0.10
    percentual = 10
elif salario_atual <= 5000:
    aumento = salario_atual * 0.07
    percentual = 7
else:
    aumento = salario_atual * 0.05
    percentual = 5

novo_salario = salario_atual + aumento

print(f"Salário atual: R${salario_atual:.2f}")
print(f"Percentual de aumento: {percentual}%")
print(f"Valor do aumento: R${aumento:.2f}")
print(f"Novo salário: R${novo_salario:.2f}")