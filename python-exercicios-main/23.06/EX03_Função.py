# Faça um programa em Python com uma função que necessite de três parametros, e que forneça:
# A soma desses três parametros através de uma função.
# Seu script também deve fornecer a média dos três números,  através de uma segunda função que chama a primeira.


def soma(n1, n2, n3):
    soma = n1+n2+n3
    return soma

def media(soma):
    media = soma/3
    return f'A média é {media:.2f}'

def main():
    nota1 = int(input("Digite a nota: "))
    nota2 = int(input("Digite a nota: "))
    nota3 = int(input("Digite a nota: "))
    somar = soma(nota1, nota2, nota3)
    return media(somar)

print(main())