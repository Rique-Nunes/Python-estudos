#02- Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas

n = 0
lista = []
par = []
impar = []

print("Digite [-99] para sair do codigo")
while n != -99:
    n = int(input("Digite o numero: "))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    lista.append(n)
lista.pop()
impar.pop()

print(f'''Lista completa: {lista}
Lista de pares {par}
Lista de impares{impar}''')