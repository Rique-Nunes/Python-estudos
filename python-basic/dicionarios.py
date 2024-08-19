# Dicionários só aceita valores imutáveis

elementos = {
    'Z': 3,
    'nome': 'Lítio',
    'grupo': 'metais alcalinos',
    'densidade': 0.534
}

# print(f'Elemento: {elementos["nome"]}')
# print(f'Densidade: {elementos["densidade"]}')
# print(f'O dicionário possui {len(elementos)}')

# Atualizar uma entrada
# elementos['grupo'] = 'Alcalinos'
# print(elementos)

# Adicionar uma entrada
# elementos['período'] = 1
# print(elementos)

# Exclusão de itens em dicionários
# del elementos['período']
# print(elementos)

# apagar todos os itens
# elementos.clear()
# print(elementos)

# del elementos deleta o dicionaio em si em vez de deixar vazio
# print(elementos)

# tipos de formatações diferentes em que se pode colocar
for i in elementos.items():  # formato básico
    print(i)

for i in elementos.keys():  # só as chaves
    print(i)

for i in elementos.values():  # só os valores
    print(i)


for i, j in elementos.items():  # i recebe as chaves e j os valores
    print(f'{i}:{j}')
