# Faça um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições:

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com a {idade} anos o voto é NEGADO'
    elif 16 <= idade < 18 or idade > 70:
        return f'Com a {idade} anos o voto é OPCIONAL'
    else:
        return f'Com a {idade} anos o voto é OBRIGATORIO'

nasc = (int(input("Digite seu ano de nascimento: ")))
print(voto(nasc))