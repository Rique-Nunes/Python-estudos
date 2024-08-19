#01 - Crie um programa que vai gerar cinco números aleatórios de 1 a 50 e colocar em uma  tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla. Sem utilizar repetições.
#Dica: utilizar a biblioteca random do Python.

from random import randint

t1 = (randint(1,50))
t2 = (randint(1,50))
t3 = (randint(1,50))
t4 = (randint(1,50))
t5 = (randint(1,50))

tupla = (t1, t2, t3, t4, t5)

print(tupla)
print(f'Numero minimo: {min(tupla)}')
print(f'Numero maximo: {max(tupla)}')