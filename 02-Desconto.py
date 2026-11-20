import os
os.system ("cls")

#Desconto de uma compra- Problemática: Uma loja dá um valor de desconto em uma compra. No código deve-se: 
#- Solicitar o valor da compra considerando: 
#-Compras a partir de 500 pilas ou mais tem 10 % de desconto;
#-Abaixo de 500 sem desconto.

#Apresentar o valor original, o valor do desconto e o valor final da compra.

#ENTRADA
produto= float (input("Informe o valor do produto:"))

#PROCESSAMENTOS
if produto >=500:
    print ("Esse produto tem desconto de 10%")
    desconto= (produto * 10) / 100
    preco_final= produto - desconto

    print ("--------------") 
    print (f"10% de {produto} é igual a {desconto}")
    print (f"Preço com desconto:R$ {preco_final:.2f}")

else:
    print ("Esse produto não tem desconto")