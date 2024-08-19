#01- Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já esteja lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

n = 0
lista = []

print("Digite [-99] para sair do codigo\n")
while n != -99:
    n = int(input("Digite o numero: "))
    if n not in lista:
        lista.append(n)
lista.pop()
lista.sort()
print(f'''Lista sem números repetidos e em ordem crescente
{lista}''') 
