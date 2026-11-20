import os
os.system ("cls")

#Faça um programa que pergunte em que turno você estuda. Peça para digitar:
#• M - Matutino
#• V - Vespertino
#• N - Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", 
#conforme o caso.

turno = input("Digite o turno em que você estuda : (Matutino/ Vespertino/ Noturno)")

if turno == "Matutino": 
    print("Bom dia!")
elif turno == "Vespertino":
    print("Boa tarde!")
elif turno == "Noturno":
    print("Boa noite!")
else:
    print("Valor Inválido.")