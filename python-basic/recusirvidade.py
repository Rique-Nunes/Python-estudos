# Recursividade

# fórmula geral para o fatorial:
# fatorial(num) = 1, se o num = 0 ou se num = 1 #caso base
# fatorial(num) = num * fatorial(num - 1), para num > 1  #caso recursivo

def fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fatorial(num-1)

if __name__ == '__main__':
    numero = int(input('Digite um número para fazer seu fatorial'))
    try:
        n = fatorial(numero)
    except RecursionError:
        print(f'O número é negativo ou muito grande para ser processado')
    else:
        print(f'o fatorial de {numero} é {n}')
