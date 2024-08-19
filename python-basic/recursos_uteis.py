# Trocar valores entre duas variáveis
var1 = 20
var2 = 31

# var2, var1 = var1, var2
# print(f'var1:{var1}, var2: {var2}')

# Operador condicional ternário
# menor = var1 if var1 < var2 else var2
# print(f'Menor valor: {menor}')
# print(f'Menor valor: {(var2, var1)[var1 <var2]}')

# Generators são constantes que somente são calculadas quando chamadas
# por isso usa tuplas em vez de listas, porem se fizesse em lista elas ficariam
# alocadas diretamente
# valores = [1, 3, 5, 7, 9, 11, 13, 15]
# quadrados = (item**2 for item in valores)
# print(quadrados)
# for valor in quadrados:
#     print(valor)


# Função enumerate()

# bebidas = ['Café', 'Chá', 'Água', 'Suco']
# for i, item in enumerate(bebidas):
#     i += 1
#     print(f'Índice: {i}, item: {item}')

# temperaturas = [-1, 10, 5, 3, 8, 4, -2, -5, 7]
# total = 0
# lista = []
# for i, t in enumerate(temperaturas):
#     if t < 0:
#         print(f'a temperatura em {i} é de {t}')
#         total += 1
#         lista.append(t)
# print(f'a o total de {total} e sendo eles {lista}')


# Gerenciamento de contexto com with
# try:
#     a = open('frutas.dat', 'r', encoding='utf-8')
#     print(a.read())
# except IOError:
#     print(f'Não foi possível abrir o arquivo')
# else:
#     a.close()

# with open('frutas.dat', 'r', encoding='utf-8') as a:
#     for linha in a:
#         print(linha.rstrip())
