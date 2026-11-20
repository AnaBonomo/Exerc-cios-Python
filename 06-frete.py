import os
os.system ("cls")

#Problema:Uma loja virtual cobra frete conforme o valor do pedido.
#Solicite o valor da compra e considere:
#Compras de R$ 300,00 ou mais: Frete grátis;
#Compras abaixo de R$ 300,00: Frete de R$ 25,00.

print ("Cálculo de frete da compra")
valor_compra = float(input("Digite o valor da compra: "))

if valor_compra >= 300:
    print("Frete grátis")

else:
    print("Frete de R$ 25,00")
    valor_compra += 25

print(f"Valor total da compra: R${valor_compra:.2f}")