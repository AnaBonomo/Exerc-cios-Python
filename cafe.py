import os
os.system ("cls")

#Para chamar a função tem que estar fora da indentação 
def preparar_cafe (tipo):
    print ("Preparando...", tipo)
    return "Seu pedido está proto."

bebida= preparar_cafe ("Com leite")
print (bebida)
