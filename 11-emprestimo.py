import os
os.system ("cls")

#Problema: Solicite o salário do cliente e o valor da parcela desejada.
#O empréstimo será aprovado somente se a parcela for menor ou igual a 30% do salário.
#Apresente:
#Empréstimo aprovado; ou
#Empréstimo não aprovado.

print ("Verificação de empréstimo")

salario = float(input("Digite o salário do cliente: R$ "))
parcela = float(input("Digite o valor da parcela desejada: R$ "))

if parcela <= (salario * 0.3):
    print("Empréstimo aprovado.")
else:
    print("Empréstimo não aprovado.")

    