import os
os.system ("cls")

#Problema:Uma empresa classifica seus clientes de acordo com o valor de compras realizadas no mês.
#Solicite o nome do cliente e o total comprado.
#Classifique:
#R$ 5.000,00 ou mais: Cliente Ouro;
#R$ 2.000,00 ou mais: Cliente Prata;
#Abaixo de R$ 2.000,00: Cliente Bronze.

print ("Classificação de clientes")
nome = input("Digite o nome do cliente: ")
total_compras = float(input("Digite o total de compras realizadas no mês: R$ "))

if total_compras >= 5000:
    print("Classificação: Cliente Ouro")

elif total_compras >= 2000:
    print("Classificação: Cliente Prata")
else:
    print("Classificação: Cliente Bronze")