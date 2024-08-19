# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma(n1, n2 , n3):
    soma = n1+n2+n3
    return soma

n1 = int(input("Coloque o primeiro número: "))
n2 = int(input("Coloque o segundo número: "))
n3 = int(input("Coloque o terceiro número: "))

soma(n1, n2 , n3)
print(f'A soma dos números é: {soma(n1, n2, n3)}')