import os
os.system ("cls")

#Problema: Solicite o peso e a altura do usuário e calcule:
#IMC = peso / altura²
#Classifique:
#IMC menor que 18,5: Abaixo do peso;
#IMC até 24,9: Peso normal;
#IMC até 29,9: Sobrepeso;
#IMC até 34,9: Obesidade Grau I;
#IMC até 39,9: Obesidade Grau II;
#IMC igual ou superior a 40: Obesidade Grau III.
#Apresente o IMC calculado e a classificação

print ("Classificação do IMC")
peso = float(input("Digite o seu peso (em kg): "))
altura = float(input("Digite a sua altura (em metros): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc <= 24.9:
    classificacao = "Peso normal"
elif imc <= 29.9:
    classificacao = "Sobrepeso"
elif imc <= 34.9:
    classificacao = "Obesidade Grau I"
elif imc <= 39.9:
    classificacao = "Obesidade Grau II"
else:
    classificacao = "Obesidade Grau III"

print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")