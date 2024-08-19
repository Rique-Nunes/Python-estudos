# Utilizando  os  conceitos  aprendidos  até dicionários,  crie  um  programa  onde  4 jogadores joguem um dado e tenham resultados aleatórios.

from random import randint
from time import sleep
import os

#Listas para cada player, onde é atribuida o dicionario do respectivo player contendo o número do dado
listap1 = []
listap2 = []
listap3 = []
listap4 = []

#Dicionario com as keys para cada player, onde é atribuido +1 a cada rodada, para verificar o player que mais venceu rodadas
play = dict()
play['Pontuacao1'] = 0
play['Pontuacao2'] = 0
play['Pontuacao3'] = 0
play['Pontuacao4'] = 0

print("\n\033[3;7m ============ BEM VINDO AO JOGO DO DADO, VAMOS TESTAR A SORTE DE NOSSOS JOGADORES ============ \033[0;0m\n")

rodadas = int(input("\033[37;1mQuantas rodadas você deseja jogar? \033[0;0m"))

print("\nJOGADORES PREPARADOS...", end=" "), print("VAMOS LÁ")
sleep(1)
os.system("cls")

for j1 in range (rodadas): #For com o número de rodadas informada pelo usuario
    #Dicionario para cada player, onde é atribuida o número gerado pelo dado, e a cada volta ele o dicionario é resetado
    player1 = dict()
    player2 = dict()
    player3 = dict()
    player4 = dict()
#=============================== PLAYER 1 ===========================================  
    print("\033[34;1;3m\nPLAYER 1 JOGOU O DADO\033[0;0m")
    sleep(0.5), print("...", end=" "), sleep(0.5), print("...", end=" "), sleep(0.5), print("...", end=" ")
    
    dado = randint(1,6) #Número aleatorio do dado
    
    print(f'\nO DADO CAIU NO NÚMERO {dado}')
    sleep(0.8)
    
    player1['Jogadas'] = dado
    listap1.append(player1['Jogadas']) #Lista do player 1 atribuindo o valor dado registrado no dicionario, e assim em diante nos proximos player (Foi feito em uma lista, para caso o programador queira ver o historico de jogadas dos player)

#=============================== PLAYER 2 =========================================== 
    print("\033[35;1;3m\nPLAYER 2 JOGOU O DADO\033[0;0m")
    sleep(0.5), print("...", end=" "), sleep(0.5), print("...", end=" "), sleep(0.5), print("...", end=" ")

    dado = randint(1,6) #Novo número gerado pelo dado, e assim em diante nos proximos players
    
    print(f'\nO DADO CAIU NO NÚMERO {dado}')
    sleep(0.8)
 
    player2['Jogadas'] = dado
    listap2.append(player2['Jogadas'])

#=============================== PLAYER 3 =========================================== 
    print("\033[36;1;3m\nPLAYER 3 JOGOU O DADO\033[0;0m")
    sleep(0.5), print("...", end=" "), sleep(0.5), print("...", end=" "), sleep(0.5), print("...", end=" ")
    
    dado = randint(1,6)

    print(f'\nO DADO CAIU NO NÚMERO {dado}')
    sleep(0.8)
    
    player3['Jogadas'] = dado
    listap3.append(player3['Jogadas'])

#=============================== PLAYER 4 =========================================== 
    print("\033[30;1;3m\nPLAYER 4 JOGOU O DADO\033[0;0m")
    sleep(0.5), print("...", end=" "), sleep(0.5), print("...", end=" "), sleep(0.5), print("...", end=" ")
    
    dado = randint(1,6)

    print(f'\nO DADO CAIU NO NÚMERO {dado}')
    sleep(0.8)

    player4['Jogadas'] = dado
    listap4.append(player4['Jogadas'])

    os.system("cls")

#Condição para verificar qual player venceu a rodada atual, usando como paremetro o dicionario que contem o número de rodadas vencidas
    if player1['Jogadas'] > player2['Jogadas'] and player1['Jogadas'] > player3['Jogadas'] and player1['Jogadas'] > player4['Jogadas']:
        play['Pontuacao1'] += 1
        print("\033[34;3;1mPLAYER 1 VENCEU A RODADA\033[0;0m")

    elif player2['Jogadas'] > player1['Jogadas'] and player2['Jogadas'] > player3['Jogadas'] and player2['Jogadas'] > player4['Jogadas']:
        play['Pontuacao2'] += 1
        print("\033[35;3;1mPLAYER 2 VENCEU A RODADA\033[0;0m")

    elif player3['Jogadas'] > player1['Jogadas'] and player3['Jogadas'] > player2['Jogadas'] and player3['Jogadas'] > player4['Jogadas']:
        play['Pontuacao3'] += 1
        print("\033[36;3;1mPLAYER 3 VENCEU A RODADA\033[0;0m")

    elif player4['Jogadas'] > player1['Jogadas'] and player4['Jogadas'] > player2['Jogadas'] and player4['Jogadas'] > player3['Jogadas']:
        play['Pontuacao4'] += 1
        print("\033[30;3;1mPLAYER 4 VENCEU A RODADA\033[0;0m")

    else:
        print("\033[37;3mHOUVE UM EMPATE,\033[0;0m \033[31;1;3mNINGUÉM\033[0;0m \033[37;3mRECEBEU PONTOS\033[0;0m")

os.system("cls")

#Condição que verifica qual player venceu mais rodadas, usando como parametro o dicionario de pontuação total
print('O GRANDE VENCEDOR FOI')
sleep(0.8), print("...", end=" "), sleep(0.8), print("...", end=" "), sleep(0.8), print("...")
if play['Pontuacao1'] > play['Pontuacao2'] and play['Pontuacao1'] > play['Pontuacao3'] and play['Pontuacao1'] > play['Pontuacao4']:
        print(f"\033[34;3;1mPLAYER 1\033[0;0m \033[32;1mVENCEU O JOGO\033[0;0m COM {play['Pontuacao1']} RODADAS VENCIDAS")

elif play['Pontuacao2'] > play['Pontuacao1'] and play['Pontuacao2'] > play['Pontuacao3'] and play['Pontuacao2'] > play['Pontuacao4']:
        print(f"\033[35;3;1mPLAYER 2\033[0;0m \033[32;1mVENCEU O JOGO\033[0;0m COM {play['Pontuacao2']} RODADAS VENCIDAS")

elif play['Pontuacao3'] > play['Pontuacao1'] and play['Pontuacao3'] > play['Pontuacao2'] and play['Pontuacao3'] > play['Pontuacao4']:
        print(f"\033[36;3;1mPLAYER 3\033[0;0m \033[32;1mVENCEU O JOGO\033[0;0m {play['Pontuacao3']} RODADAS VENCIDAS")

elif play['Pontuacao4'] > play['Pontuacao1'] and play['Pontuacao4'] > play['Pontuacao2'] and play['Pontuacao4'] > play['Pontuacao3']:
        print(f"\033[30;3;1mPLAYER 4\033[0;0m \033[32;1mVENCEU O JOGO\033[0;0m {play['Pontuacao4']} RODADAS VENCIDAS")
else:
    print("\033[31mHOUVE UM EMPATE, DADO A ISSO NÃO TEMOS UM VENCEDOR NESTA PARTIDA!")
