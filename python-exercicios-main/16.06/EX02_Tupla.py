#02 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.

qtnd = pos = 0

tupla = int(input("Digite um número: ")), int(input("Digite um número: ")), int(input("Digite um número: ")), int(input("Digite um número: "))

qtnd = tupla.count(9)
pos = tupla.index(3)

print(f'Quantidade de números nove: {qtnd}')
print(f'Posição do número três: {pos}')