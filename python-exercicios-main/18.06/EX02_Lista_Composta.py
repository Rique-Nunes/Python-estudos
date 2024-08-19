#02 - Aprimore o desafio anterior, mostrando no final:
#    A) A soma de todos os valores pares digitados.
#    B) A soma dos valores da terceira coluna. 
#    C) O maior valor da segunda linha.

lista = list()
par = 0
coluna3 = 0

for c in range(0,3):
    n = list()
    print(f'Linha {c+1}')
    valor = (int(input("Digite o primeiro valor: ")))
    n.append(valor)    
    if valor % 2 == 0:
        par += valor
    valor = (int(input("Digite o primeiro valor: ")))
    n.append(valor)
    if valor % 2 == 0:
        par += valor
    valor = (int(input("Digite o primeiro valor: ")))
    n.append(valor)
    if valor % 2 == 0:
        par += valor
    lista.append(n[:])

print(f'A soma de todos os pares da lista: {par}')

coluna3 = lista[0][2] + lista[1][2] + lista[2][2]
print(f'Soma das números da terceira coluna: {coluna3}')

max = max(lista[1][0], lista[1][1], lista[1][2])
print(f'Maior valor da segunda linha: {max}')