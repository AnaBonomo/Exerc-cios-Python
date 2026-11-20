import os
os.system ("cls")

#Faça um programa que leia 5 números e informe o maior número

maior= int(input("Digite o 1º número: "))

for i in range(2, 6):
    numero = int(input(f"Digite o {i}º número: "))
    if numero > maior:
        maior = numero
        
print(f"O maior número é: {maior}")