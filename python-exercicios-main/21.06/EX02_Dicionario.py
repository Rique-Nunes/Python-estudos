# 2. Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os com idade em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade , com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.

trab = dict()
trab ['Nome'] = str(input("Nome: "))
nasc = int(input("Ano de nascimento: "))
idade = 2021 - nasc
trab ['Idade'] = idade
trab ['Carteira'] = int(input("CTPS (Sem traço e estado) (Digite 0 caso não tenha): "))
if trab['Carteira'] != 0:
    trab['AnoContratacao'] = int(input("Ano de contratação: "))
    trab['Salario'] = float(input("Salario: "))

aposentadoria = trab['Idade'] + 35

trab['Aposentadoria'] = aposentadoria

print(f'''\nNome: {trab['Nome']}
\nIdade: {trab['Idade']}
\nCarteira: {trab['Carteira']}''')
if trab ['Carteira'] != 0:
    print(f'''\nAno de contratação: {trab['AnoContratacao']}
\nSalario: {trab['Salario']}
\nVocê ira se aposentar com {trab['Aposentadoria']} anos''')
