import os
os.system ("cls")

#Problema:Solicite o valor da compra e a forma de pagamento.
#Considere:
#1 – PIX: 10% de desconto;
#2 – Dinheiro: 5% de desconto;
#3 – Cartão: sem desconto.
#Apresente o valor final da compra.

print ("Cálculo de desconto da compra")
valor_compra = float(input("Digite o valor da compra: "))
print("Escolha a forma de pagamento:")
print("1 - PIX (10% de desconto)")
print("2 - Dinheiro (5% de desconto)")
print("3 - Cartão (sem desconto)")

forma_pagamento = int(input("Digite o número correspondente à forma de pagamento: "))

if forma_pagamento == 1:
    desconto = valor_compra * 0.10
    valor_final = valor_compra - desconto
    print(f"Desconto de 10% aplicado. Valor final da compra: R${valor_final:.2f}")
elif forma_pagamento == 2:
    desconto = valor_compra * 0.05
    valor_final = valor_compra - desconto
    print(f"Desconto de 5% aplicado. Valor final da compra: R${valor_final:.2f}")
elif forma_pagamento == 3:
    print(f"Sem desconto. Valor final da compra: R${valor_compra:.2f}")
else:
    print("Forma de pagamento inválida.")


        