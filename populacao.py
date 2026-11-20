import os
os.system("cls")

#Supondo que a população de um país A seja da ordem de 80_000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200_000
#habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse 
#ou iguale a população do país B, mantidas as taxas de crescimento.

for i in range(1, 100):
    pais_a = 80000 * (1 + 0.03) ** i
    pais_b = 200000 * (1 + 0.015) ** i
    if pais_a >= pais_b:
        print(f"Serão necessários {i} anos para que a população do país A ultrapasse ou iguale a população do país B.")
        break  

print(f"População do país A após {i} anos: {pais_a:.0f}")
print(f"População do país B após {i} anos: {pais_b:.0f}")