# São imutáveis / Listas -> [] / Tuplas -> ()

# halogenios = ('F', 'Cl', 'Br', 'I', 'At')
# gases_nobres = ('he', 'he', 'Ar', 'Xe', 'Kr', 'Rn')
# elementos = halogenios + gases_nobres

# print(elementos)
# t1 = (1, 2, 3, 4, 5, 6, 78, 1, 2, 34, 56, 7, 78, 5, 5, 5)
# print(t1.count(5)) Contar quantos elementos 5 possue

# print(halogenios[-2]) da pra pegar as posições como nas listas
# print('Cl' in halogenios) da pra verificar se algo está dentro da tupla como nas listas
# print(sum(t1)) somando todos os itens da tupla
# print(min(t1)) o menor valor da tupla
# print(max(t1)) o maior valor da tupla

# Operações não disponíveis em tuplas: .sort(), .append(), .reverse(), pop()... coisas que mudam os valores...
# for elemento in elementos:
#     print(f"elemento: {elemento}")

# grupo17 = list(halogenios) transforma a tupla em uma lista
# grupo17[0] = 'H'
# print(type)

# grupo1 = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
# alcalinos = tuple(grupo1) transforma a lista em uma tupla
# print(type(alcalinos))

# print(sorted(alcalinos))
# print(alcalinos.sort())
