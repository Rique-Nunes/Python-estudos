#Crie uma lista composta que recebe 5 nomes e 5 idades de clientes, utilizando o for e o if, verifique quais clientes são maiores de idade e quais são menores de idade e mostre na tela a seguinte frase para cada um deles: 'Fulano é maior de idade' ou 'Fulana é menor de idade' e  também quantos são maiores e quantos são menores de idade.


galera = list()
total_maior = total_menor = 0

for c in range(5):
    dado = list()
    dado.append(str(input("Digite o nome: ")))
    dado.append(int(input("Digite o idade: ")))
    galera.append(dado[:])
print(galera)

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        total_maior += 1
    else:
        print(f'{p[0]} é menor de idade')
        total_menor +=1