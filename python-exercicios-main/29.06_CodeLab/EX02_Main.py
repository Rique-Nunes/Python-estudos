#Vamos aprimorar o código: cadastro de jogador de futebol.py que foi desenvolvido no Code Lab da aula14. Faça com que o seu código funcione para vários jogadores,incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador

from EX02_Jogadores import Jogador

jogadores = list()

while True:
    jogador = Jogador(str(input("Nome: ")), int(input("Partidas jogadas: ")), int(input("Gols Total no Campeonato: ")))
    print(jogador.aproveitamento())
    jogadores.append(jogador)
    saida = str(input("Deseja sair? [S/N] ")).upper().strip()[0]
    if saida == "S":
        break

print(jogadores[0].aproveitamento()) 