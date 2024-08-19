# funções
# Modularização, Reúso de Código, Legibilidade

# def <nome_função> ([argumentos]):
#     <instruções>

# def mensagem():
#     print('Bóson treinamentos em tecnologia')
#     print('Curso completo de Python.')

# def soma(n1, n2):
#     somando = n1+n2
#     print(somando)
# soma(12, 7)


# def mult(x, y):
#     return x*y
# a = 5
# b = 8
# c = mult(a, b)
# print(c)


# def quadrado(val):
#     quadrados = []
#     for x in val:
#         quadrados.append(x ** 2)
#     return quadrados

# if __name__ == '__main__':
#     valores = [2, 3, 45, 6, 2, 1, 4, 5]
#     resultados = quadrado(valores)

#     for i in range(len(valores)):
#         print(f"{valores[i]}:{resultados[i]}")


# def contar(caractere, num=11):
#     for i in range(1, num):
#         print(caractere)
# x, y, z = 5, 8, 6


# def soma_mult(a, b, c=0):
#     if c == 0:
#         return a*b
#     else:
#         return a+b+c


# if __name__ == '__main__':
#     res = soma_mult(x, y, z)
#     print(res)


# def identificador(numero):
#     if numero > 0:
#         return "positivo"
#     else:
#         return "negativo"
# num = int(input("digite um numero"))
# num2 = int(input("digite o segundo numero"))
# asoma = soma(num, num2)

# print(f"esse numero é {identificador(asoma)}, a sua soma é {asoma}")

# def categoria(idade):
#     if 0 >= idade:
#         return "idade inválida"
#     elif 5 <= idade <= 7:
#         return "Infantil A"
#     elif 8 <= idade <= 10:
#         return "Infantil B"
#     elif 11 <= idade <= 13:
#         return "Juvenil A"
#     elif 14 <= idade <= 17:
#         return "Juvenil B"
#     else:
#         return "Adulto"


# idade = int(input("Escreva a idade: "))
# lutador = categoria(idade)
# print(lutador)


# dia = int(input("Diga seu dia"))
# mes = int(input("Diga seu mês"))
# ano = int(input("diga seu ano"))


# def meses(mes):
#     if mes <= 0:
#         return "número inválido"
#     elif mes == 1:
#         return "Janeiro"
#     elif mes == 2:
#         return "fevereiro"
#     elif mes == 3:
#         return "março"
#     elif mes == 4:
#         return "abril"
#     elif mes == 5:
#         return "maio"
#     elif mes == 6:
#         return "junho"
#     elif mes == 7:
#         return "julho"
#     elif mes == 8:
#         return "agosto"
#     elif mes == 9:
#         return "setembro"
#     elif mes == 10:
#         return "outubro"
#     elif mes == 11:
#         return "novembro"
#     elif mes == 12:
#         return "dezembro"
#     else:
#         return "erro"


# print(f"voce nasceu em {dia}, {meses(mes)} ,{ano}")
