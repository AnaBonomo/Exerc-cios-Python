import os
os.system ("cls")

#Desenvolva um programa que solicite o nome do vendedor e o valor total vendido no mês.
#Classifique o desempenho:
#R$ 15.000,00 ou mais: Excelente;
#R$ 10.000,00 ou mais: Meta atingida;
#Abaixo de R$ 10.000,00: Meta não atingida.

print ("Classificação de desempenho do vendedor")
nome = input("Digite o nome do vendedor: ")
vendas = float(input("Digite o valor total vendido no mês: "))

if vendas >= 15000:
    print("Desempenho: Excelente")
elif vendas >= 10000:
    print("Desempenho: Meta atingida")
else:
    print("Desempenho: Meta não atingida")  