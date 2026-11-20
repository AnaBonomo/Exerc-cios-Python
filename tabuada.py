import os
os.system("cls")

#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada.

print ("Tabuada com for")

numero= int (input("Digite um número para ver a tabuada: "))

for i in range (1,11):
    print (f"{numero} x {i} = {numero*i}")

print ("______________________")    

print ("Tabuada em While")

numero= int (input("Digite um número para ver a tabuada: "))
i=1

while i<=10:
    print (f"{numero}x{i} = {numero*i}")
    i+=1