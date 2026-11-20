import os
os.system ("cls")

#Faça um programa que pergunte quanto você ganha por hora e o número de horas 
#trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

#Entrada
hora = float(input("Informe quanto você ganha por hora: "))
horas_trabalhadas = float(input("Informe o número de horas trabalhadas no mês: "))

#Processamento
salario_total = hora * horas_trabalhadas

#Saída
print(f"O total do seu salário no referido mês é: R$ {salario_total:.2f}")