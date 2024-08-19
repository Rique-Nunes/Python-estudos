# funções lambda (anônimas)
# Sintaxe:
# lamda argumentos: expressão

# quadrado = lambda x: x**2

# for i in range(1, 11):
#      print(quadrado(i))

# par = lambda x: x%2 == 0
# print(par(9))

# f_c = lambda f: (f-32) * 5/9
# print(f_c(32))

# função map
# num = [1, 2, 3, 4, 5, 6, 7]
# dobro = list(map(lambda x: x**2, num))
# print(dobro)

# palavras = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']
# maiusculas = list(map(str.lower, palavras))
# print(maiusculas)

# função filter
# def pare(num):
#     return num % 2 == 0

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12]
# num_par = list(filter(pare, numeros))
# print(num_par)

# num_impar = list(filter(lambda x: x % 2 != 0, numeros))
# print(num_impar)

# função reduce
# from functools import reduce

# def mult(x, y):
#     return x*y

# numeros = [1, 2, 3, 4, 5, 6, 78]
# total = reduce(mult, numeros)
# print(total)

# soma cumulativa dos quadrados de valores usando labda
# numeros = [1, 2, 3, 4, 5, 6]
# ((1² + 2²)² +3²)² + 4²
# total = reduce(lambda x, y: x**2 + y**2, numeros)
# print(total)
