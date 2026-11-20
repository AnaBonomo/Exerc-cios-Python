import os
os.system ("cls")

#Fazer um programa que leia duas notas de um aluno, calcule e mostre a sua média. 
# A mensagem "Aprovado" se a média for maior ou igual a 7, 
# "Reprovado" se a média for menor que 7
# "Aprovado com Distinção" se a média for igual a 10.

print ("Notas alunos")
trabalho= float (input("Informe a nota de trabalho:"))
prova= float (input("Informe a nota da prova:"))

media= (trabalho + prova) / 2
print ("A média do aluno é: ", media)

if media == 10:
    print ("Aprovado com Distinção")        
    if media >= 7:
        print ("Aprovado")
else:
    print ("Reprovado")