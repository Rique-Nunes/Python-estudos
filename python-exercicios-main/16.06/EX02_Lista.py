# Desafio da noite:
# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".

lista = []
soma = 0

p = str(input("Telefonou para a vítima? ")).strip().upper()[0], str(input("Esteve no local do crime? ")).strip().upper()[0], str(input("Mora perto da vítima? ")).strip().upper()[0], str(input("Devia para a vítima? ")).strip().upper()[0], str(input("Já trabalhou com a vítima? ")).strip().upper()[0]

for n in p:
    if n == "S":
        lista += [1]
        soma = sum(lista)

if soma == 2:
    print("\nSuspeito")
elif soma == 3 or soma == 4:
    print("\nCumplice")
elif soma == 5:
    print("\nAssasino")
else:
    print("\nInocente")