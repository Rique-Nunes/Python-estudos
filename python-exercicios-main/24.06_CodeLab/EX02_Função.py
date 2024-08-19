# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, ‘N’, se seu argumento for negativo e ‘0’ se for 0.

def numero(n1):
    if n1 < 0:
        return f'Seu número é negativo'
    elif n1 > 0:
        return f'Seu número é positivo'
    else:
        return f'Seu número é neutro'

n1 = int(input("Digite seu número: "))
numero(n1)

print(numero(n1))