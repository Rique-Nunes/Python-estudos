#Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles forem iguais, imprima que eles são iguais.

def numbers(n1,n2):
    if n1 == n2:
        return f'Os números são iguais'
    elif n1 > n2:
        numbers = n1
        return f'O maior é o número {numbers}'
    else:
        numbers = n2
        return f'O maior é o número {numbers}'

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

print(numbers(n1,n2))