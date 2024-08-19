#01 - Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com essa formatação:
# [  1  ][  2  ][  3  ]
# [  4  ][  5  ][  6  ]
# [  7  ][  8  ][  9  ] 

# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

lista = list()

for c in range(0,3):
    n = list()
    print(f'Linha {c+1}')
    n.append(int(input("Digite o primeiro valor: ")))
    n.append(int(input("Digite o segundo valor: ")))
    n.append(int(input("Digite o terceiro valor: ")))
    lista.append(n[:])
print(f'''\n[ {lista[0][0]} ][ {lista[0][1]} ][ {lista[0][2]} ]
[ {lista[1][0]} ][ {lista[1][1]} ][ {lista[1][2]} ]
[ {lista[2][0]} ][ {lista[2][1]} ][ {lista[2][2]} ]''')
print(f'\n{lista}')