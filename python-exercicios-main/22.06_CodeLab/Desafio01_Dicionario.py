#5.DESAFIO:Crie um programa que leia nome, sexobiologicoe idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:A) Quantas pessoas estão cadastradas.B) A média da idade.C) Uma lista com as mulheres.D) Uma lista com as idades que estão acima da média.OBS: O programa deve garantir que o sexo digitado seja válido, e que quando perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.

saida = ""
listaT = []
listaMulheres = []
listaMedia = []
pessoas = 0
media = 0
mediaFinal = 0

while True:
    saida = str(input("\nDESEJA SAIR [SIM/NAO]: ")).upper().strip()
    dicionario = dict()
    if saida in "SIM":
        break
    else:
        dicionario["Nome"] = str(input("\nNome: "))
        dicionario["SexoBiologico"] = str(input("Sexo Biologico: [M/F]")).strip().upper()[0]
        dicionario["Idade"] = int(input("Idade: "))
        listaT.append(dicionario.copy())
        pessoas += 1
        media += dicionario["Idade"]

    if dicionario['SexoBiologico'] not in "MF":
            print("\nSEXO BIOLOGICO INVALIDO")
            break

    if dicionario["SexoBiologico"] == "F":
        listaMulheres.append(dicionario.copy())

    mediaFinal = media/pessoas

    if dicionario["Idade"] > mediaFinal:
        listaMedia.append(dicionario.copy())
     

print(f'''Lista total: {listaT}
Foram cadastradas um total de {pessoas} pessoas
A media das idades é: {mediaFinal}
Lista de mulheres: {listaMulheres}
Lista de pessoas com idade acima de média: {listaMedia}''')