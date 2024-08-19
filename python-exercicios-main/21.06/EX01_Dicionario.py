aluno = dict()
aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input(f'Média do {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situacao'] = "Aprovado"
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = "Recuperação"
else:
    aluno['situacao'] = "Reprovado"

for k , v in aluno.items():
    k = k.title()
    if k == "Media":
        k = k.replace("e" , "é")
    print(f'{k} é igual a {v}')
