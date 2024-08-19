#02-Crie um programa que pergunte ao usuário um número inteiro e faça a tabuada desse número.

numero = int(input("Digite um número para o calculo: "))

for n in range(0,11):
   print(f'{n} X {numero} = {n * numero}')
