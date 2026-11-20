import os
os.system ("cls")

print ("B.O-1: argumentação mensagem")
def escreva (msg):
    print (msg)
print ("Olá mundo!")   
print ("Não faz omenor sentido definir o valor de uma variavel depois dela")

print ("------------------")

print ("B.O-2: argumentação cálculo")
def soma (n1,n2):
    print (n1 + n2)

soma (1,2)
soma (3,4)
soma (9,7)
soma (23,7)
soma (10,8)

print ("--------------")

#declação de função
#com argumento e retorno
#Returno, ele volta somente para o código, serve somente para o código, não exibe a linha 32, pois nõa foi pedido, não foi "printado"
#Só fica guardado, para ser reutilizado em outro código

def soma (n1,n2):
    return n1+n2
print (soma(6,2))
soma (3,3)