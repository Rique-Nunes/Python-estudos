# Exceção é um objeto que representa um erro que
# ocorreu ao executar o programa
# Blocos Try ... except

# def div(k, j):
#     return round(k/j, 2)


# if __name__ == '__main__':
#     while True:
#         try:
#             n1 = int(input("Digite um número: "))
#             n2 = int(input("digite outro numero: "))
#             break
#         except ValueError:
#             print('ocorreu um erro ao ler o valor: tente novamente')

#     try:
#         r = div(n1, n2)
#     except ZeroDivisionError:
#         print("não é possivel dividir por zero")
#     except:
#         print('erro desconhecido')
#     else:
#         print(f'Resultado: {r}')
#     finally:
#         print("\nobrigado pela preferencia")

from math import sqrt

if __name__ == '__main__':
    try:
        num = int(input('Digite um número positivo: '))
        if num < 0:
            raise ArithmeticError
    except ArithmeticError:
        print(f'Foi fornecido um número negativo')
    else:
        print(f'A raiz quadrada de {num} é {sqrt(num)}')
    finally:
        print("fim do processo!")
