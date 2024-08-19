# Sets colecoes nao ordenadas de valores únicos,
# itens não duplicados e operações matematica sobre conjuntos

# planeta_anao = {'Plutão', 'Ceres', 'Eris', 'Haumeia', 'Makemake'}
# print(len(planeta_anao))
# print('Lua' not in planeta_anao)

# for astro in planeta_anao:
#     print(astro.upper(), end=', ') da para tratar os itens separadamente

# astros = ['Lua', 'Lua', 'Venus', 'Sirius', 'Marte']
# print(astros, end=' ')
# astro_set = set(astros)   transformando lista em sets
# print(astro_set)

astros1 = {'Lua', 'Venus', 'Sirius', 'Marte'}
astros2 = {'Lua', 'Venus', 'Sirius', 'Marte', 'Cometa Harley'}
# print(astros1 | astros2)
# print(astros1.union(astros2)) #União

# print(astros1 & astros2)
# print(astros1.intersection(astros2)) #Interseção

# print(astros1 ^ astros2)
# print(astros1.symmetric_difference(astros2)) #simularidade

astros1.add('Urano')
astros1.add('Sol')
# astros1.discard('Venus')
astros1.remove('Venus')
# astros1.clear
astros1.pop()  # remove algo aleatório
print(astros1)
