import os
os.system ("cls")

#Problema:Desenvolva um programa que solicite o nome de um produto e a quantidade disponível no estoque.
#Classifique:
#Menos de 10 unidades: Estoque crítico;
#De 10 a 30 unidades: Estoque baixo;
#Acima de 30 unidades: Estoque adequado.

print ("Classificação de estoque do produto")
nome = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade disponível no estoque: "))

if quantidade < 10:
    print("Classificação: Estoque crítico")
elif quantidade <= 30:
    print("Classificação: Estoque baixo")
else:
    print("Classificação: Estoque adequado")