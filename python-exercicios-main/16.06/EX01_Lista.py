# 01 - Dada a lista l = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# a) tamanho da lista.
# b) maior valor da lista.
# c) menor valor da lista.
# d) soma de todos os elementos da lista.
# e) lista em ordem crescente.
# f) lista em ordem decrescente.

lista = [5, 7, 2, 9, 4, 1, 3]

a = len(lista)
b = max(lista)
c = min(lista)
d = sum(lista)

print(f'''Tamanho da lista: {a}
Maior valor: {b}
Menor valor: {c}
Soma dos valores: {d}''')

lista.sort()
print(f'Lista em ordem crescente: {lista}')

lista.sort(reverse=True)
print(f'Lista em ordem decrescente: {lista}')
