import os
os.system("cls")

#Fazer das 4 notas bimestrais e mostrar a média.

#Entrada
nota1 = float(input("Informe a nota do 1° bimestre: "))
nota2 = float(input("Informe a nota do 2° bimestre: "))
nota3 = float(input("Informe a nota do 3° bimestre: "))
nota4 = float(input("Informe a nota do 4° bimestre: "))

#Processamento
media = (nota1 + nota2 + nota3 + nota4) / 4

#Saída    
print(f"A média do aluno é: {media:.2f}")