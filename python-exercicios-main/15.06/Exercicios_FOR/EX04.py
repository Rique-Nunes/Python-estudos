#04-Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o. Mostre também quantos valores pares foram digitados.

par = 0
parCont = 0

for c in range (0,6):
    c = int(input("Digite um numero: "))
    if c % 2 == 0:
        parCont += c
        par += 1
print(f'Você digitou {par} números pares e a soma deles é: {parCont}') 