import os
os.system("cls")

num= int (input ("Digite um valor para ver os multiplos de 3:"))

for i in range (3,num+1,3):
    print (f"multiplos de 3: {i}")


print("_________________________________________")

print(" Multiplos de 3:")

i=3
num= int (input ("Digite um valor:"))

for i in range (3,num+1,3):
    print (f"multiplo de 3: {i}")

print("_________________________________________")

print ("Agora em While")

i=3
num= int (input ("Digite um valor:"))
while i <= num:
    print (f"multiplo de 3: {i}")
    i+=3
