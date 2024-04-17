# Crie uma função em python que receba um número diga se o número é par ou ímpar.

def par_impar(num):
    if num % 2 == 0:
        print(f"{num} é par")
    else:
        print(f"{num} é ímpar")
    
par_impar(5)
par_impar(4)