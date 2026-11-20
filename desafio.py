import os
os.system ("cls")

#Problema:Uma loja deseja automatizar uma venda.
#Solicite:
#Nome do cliente;
#Nome do produto;
#Preço unitário;
#Quantidade.
#Calcule o subtotal e aplique:
#Subtotal acima de R$ 1.000,00: 15% de desconto;
#Subtotal acima de R$ 500,00: 10% de desconto;
#Subtotal acima de R$ 200,00: 5% de desconto;
#Até R$ 200,00: sem desconto.
#Apresente o cliente, produto, subtotal, percentual de desconto, valor do desconto e total a pagar.

print ("Cálculo de venda")

nome_cliente = input("Digite o nome do cliente: ")
nome_produto = input("Digite o nome do produto: ")
preco_unitario = float(input("Digite o preço unitário do produto: R$ "))
quantidade = int(input("Digite a quantidade do produto: "))

subtotal = preco_unitario * quantidade

if subtotal > 1000:
    desconto = subtotal * 0.15
    percentual = 15
elif subtotal > 500:
    desconto = subtotal * 0.10
    percentual = 10
elif subtotal > 200:
    desconto = subtotal * 0.05
    percentual = 5
else:
    desconto = 0
    percentual = 0

total_a_pagar = subtotal - desconto

print(f"Cliente: {nome_cliente}")
print(f"Produto: {nome_produto}")
print(f"Subtotal: R${subtotal:.2f}")
print(f"Percentual de desconto: {percentual}%")
print(f"Valor do desconto: R${desconto:.2f}")
print(f"Total a pagar: R${total_a_pagar:.2f}")
