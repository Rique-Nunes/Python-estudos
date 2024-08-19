def fatorial(num):
    if num < 0:
        return 'Digite um valor maior ou igual a zero'
    else:
        if num == 0 or num == 1:
            return 1
        else:
            valor = 1
            for i in range(num, 1, -1):
                valor *= i
            return valor


def fibo(n):
    resultado = []
    a, b = 0, 1
    while b <= n:
        resultado.append(b)
        a, b = b, a + b
    return resultado



