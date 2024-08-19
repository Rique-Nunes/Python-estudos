#4.Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade , com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.

trab = dict()
trab['Nome'] = str(input("Nome: "))
Nasc = int(input("Ano de nascimento: "))
trab['Idade'] = 2021 - Nasc
trab['CTPS'] = input("CTPS: ")

if trab['CTPS'] != 0:
    trab['AnoContratacao'] = int(input("Ano de contratação: "))
    trab['Salario'] = float(input("Sálario: "))

contribuicao = trab['Idade'] + 35
trab['Aposentadoria'] = contribuicao

print(f'''Nome: {trab['Nome']}
Idade: {trab['Idade']}
CTPS: {trab['CTPS']}''')

if trab['CTPS'] != 0:
    print(f'''Ano de contratação: {trab['AnoContratacao']}
Salario: {trab['Salario']}
Você irá se aposentar com {trab['Aposentadoria']} anos''')