import os
os.system ("cls")

#Problema:Uma empresa paga comissão de acordo com o total de vendas.
#Solicite o nome do vendedor e o valor das vendas.
#Regras:
#Vendas acima de R$ 20.000,00: comissão de 10%;
#Vendas acima de R$ 10.000,00: comissão de 7%;
#Demais vendas: comissão de 5%.
#Apresente o valor vendido, o percentual de comissão e o valor da comissão

print ("Cálculo de comissão do vendedor")
nome = input("Digite o nome do vendedor: ")
vendas = float(input("Digite o valor total vendido no mês: "))      

if vendas > 20000:
    comissao = vendas * 0.10
    percentual = 10
elif vendas > 10000:
    comissao = vendas * 0.07
    percentual = 7          
else:
    comissao = vendas * 0.05
    percentual = 5  

print(f"Vendas: R${vendas:.2f}")
print(f"Percentual de comissão: {percentual}%")
print(f"Valor da comissão: R${comissao:.2f}")   
        