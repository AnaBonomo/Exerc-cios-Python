import os
os.system ("cls")

#Problema: Uma empresa recebeu orçamento de dois fornecedores.
#Solicite:
#Nome do fornecedor 1 e valor da proposta;
#Nome do fornecedor 2 e valor da proposta.
#Informe qual fornecedor apresentou o menor preço.
#Se os valores forem iguais, informe: “As propostas possuem o mesmo valor.”

print ("Comparação de preços entre fornecedores")

fornecedor1 = input("Digite o nome do fornecedor 1: ")
valor1 = float(input("Digite o valor da proposta do fornecedor 1: R$ "))
fornecedor2 = input("Digite o nome do fornecedor 2: ")
valor2 = float(input("Digite o valor da proposta do fornecedor 2: R$ "))

if valor1 < valor2:
    print(f"O fornecedor {fornecedor1} apresentou o menor preço: R${valor1:.2f}")

elif valor2 < valor1:
    print(f"O fornecedor {fornecedor2} apresentou o menor preço: R${valor2:.2f}")

else:
    print("As propostas possuem o mesmo valor.")

print("Fim da comparação de preços.")