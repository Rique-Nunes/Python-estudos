#Faça um programa, com uma função que necessite de um parametro. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def numero(n1):
    if n1 > 0:
        return f'Seu número {n1} é positivo'
    elif n1 < 0:
        return f'Seu número {n1} é negativo'
    else:
        return f'Seu número {n1} é neutro'

number = int(input("Digite um número: "))
print(numero(number))