import os
os.system ("cls")
import time

num=5
i=1
while i<=10:
    print(f"{num} x {i} = {num*i}")
    i+=1 # Incrementa o valor de i em 1 a cada iteração

    time.sleep(2) # Pausa a execução por 2 segundos para melhor visualização
 