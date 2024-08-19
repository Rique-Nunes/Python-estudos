#3.Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela. A média para aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é reprovado.

aluno = dict()

aluno['Nome'] = str(input("Nome: "))
aluno ['Media'] = float(input("Media: "))

if aluno['Media'] >= 7:
    aluno['Situacao'] = "Aprovado"
elif 5 >= aluno['Media'] < 7:
    aluno['Situacao'] = "Recuperação"
else:
    aluno['Situacao'] = "Reprovado"

for k, v in aluno.items():
    print(f'{k} = {v}')