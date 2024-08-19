#Faça um programa que ajude um jogador da MEGA SENA a criar palpites. 
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint


n = 0
jogos = 0
lista = []
listaFinal = []

jogos = int(input("Quantos jogos serão gerados: "))
for i in range (jogos):
    lista = []
    for p in range(0,6):
        n = (randint(1,60))
        lista.append(n)
    listaFinal.append(lista)
    print(f'Jogo {i + 1}: {listaFinal[i]}')