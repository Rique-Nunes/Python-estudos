#Escreva uma função que, dado um número nota representando a nota de um estudante, converte o valor de nota para um conceito (A, B, C, D, E e F).

def nota(n1):
    nota = n1
    if nota > 9.0:
        nota = 'A'
        return nota
    elif nota >=8:
        nota = 'B'
        return nota
    elif nota >= 7:
        nota = 'C'
        return nota
    elif nota >= 6:
        nota = 'D'
        return nota
    elif nota >= 5:
        nota = 'E'
        return nota
    else:
        nota = 'F'
        return nota

n1 = float(input("Digite sua nota: "))

print(f'Sua nota é equivalente ao conceito: {nota(n1)}')