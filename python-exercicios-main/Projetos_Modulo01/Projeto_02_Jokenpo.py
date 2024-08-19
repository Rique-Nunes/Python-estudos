from random import randint
from time import sleep
import os

pedra = '''  `.--.`                 
            .+sss+/::/oss-              
      .++/oyo-     `.   `h+             
    .ho-sh-         `/+oooNso+:`        
   `m- ho                `.` `:h/       
   so /h /ssss+                `N       
  `N` m: +:.`                 .yo       
  .N `M` -:/osss:        -/+ooyd-       
   yo`M``oys/.                 .N`      
    /osh`   -/`                `N`      
       -h/                  ``:h/       
         /yo.          `-/++dh:`        
           .+ss+:.`      .:sy`          
               `:/+osoooo+:`            
                                        
                                        '''
tesoura = '''  
  `//+++///////++.            
 :s.+o.      `- `s:           
:s`y--++/`    `//+h/:--.`     
h s-`++-`           `.--://+: 
o+d /o--+:                  +/
  +/  :-        .:/+yy+/////o-
   +o`               `/++.    
    `++-     `-//:`      :s.  
       -///////+/.:++/.   `h  
                      :++/o-  
                      '''
papel = '''

                .+///+-       
    ``        `++`   /+       
  //:://`    -o.   .o:`-//:.  
  o:   -s  -+:    /y+/:-  `/o 
  `s-   h:+:    `oo-`   `.:+- 
   .y   --     `/`    -//:-`  
   :+              `:ss+/:::+:
  -y:  --  `      `/.`   .-:+:
 `y/o`+:-/+-         -://:.`  
  y./o`/////`     -//-``      
  `o/.o/-.`   .:/+-`          
    .+/+s/////-`              
'''
escolha = " " #Escolha do usuario
saida = " " #Variavel de saida do While

vitoriasJogador = 0 #Variaveis que contam as vitorias
vitoriasMaquina = 0

print("\n\033[3;7mBEM VINDO AO FAMOSO JOGO DO PEDRA, PAPEL OU TESOURA, OU PARA OS INTIMOS O FAMOSO JOKENPÔ, VAMOS JOGAR!\033[0;0m\n")

while saida not in "N": #Enquanto o usuario nao digitar N o codigo continua rodando
    rodadas = int(input("Quantas rodadas iremos jogar? ")) #Coleta o número de jogadas que o usuario quer jogar
    for j in range (rodadas): #For para fazer o looping com base no número de jogadas que o usuario escolher
        escolha = str(input("Qual sua escolha? \033[1;30m[PE - PEDRA]\033[0;0m \033[1;37m[PA - PAPEL]\033[0;0m \033[1;33m[TE - TESOURA]\033[0;0m: ")).strip().upper()[0:2]
        os.system("cls")
        maquina = randint(1,3) #Escolhe um número aleatoria de 1 a 3. 1 = Pedra 2 = Papel, 3 = Tesoura
        sleep(0.8)
        if escolha in "PE": #IF para Pedra
            print("\n\033[4;93mPEDRA", end=" ")
            sleep(0.7)
            print("PAPEL", end=" ")
            sleep(0.7)
            print("TESOOOOU", end="")
            sleep(1)
            print("RA\n\033[0;0m")
            if maquina == 1:
                sleep(0.3)
                print(f'''SUA ESCOLHA:
                {pedra}''')
                print(f'''ESCOLHA DA MAQUINA:
                {pedra}''')
                print("\n\033[4;36mDESSA VEZ FOI EMPATE!\033[0;0m")
            elif maquina == 2:
                sleep(0.3)
                print(f'''SUA ESCOLHA:
                {pedra}''')
                print(f'''ESCOLHA DA MAQUINA:
                {papel}''')
                print("\n\033[4;31mVOCÊ PERDEU! QUE AZAR\033[0;0m")
                vitoriasMaquina += 1
            else:
                sleep(0.3)
                print(f'''SUA ESCOLHA:
                {pedra}''')
                print(f'''ESCOLHA DA MAQUINA:
                {tesoura}''')
                print("\n\033[4;32mVOCÊ GANHOU! PARECE QUE VOCÊ ESTÁ COM SORTE\033[0;0m")
                vitoriasJogador += 1

        if escolha in "PA": #If para Papel
            sleep(0.6)
            print("\n\033[4;93mPEDRA", end=" ")
            sleep(0.7)
            print("PAPEL", end=" ")
            sleep(0.7)
            print("TESOOOOU", end="")
            sleep(1)
            print("RA\n\033[0;0m")
            if maquina == 1:
                sleep(0.3)
                print(f'''SUA ESCOLHA:
                {papel}''')
                print(f'''ESCOLHA DA MAQUINA:
                {papel}''')
                print("\n\033[4;36mDESSA VEZ FOI EMPATE!\033[0;0m")
            elif maquina == 2:
                sleep(0.3)
                print(f'''SUA ESCOLHA:
                {papel}''')
                print(f'''ESCOLHA DA MAQUINA:
                {tesoura}''')
                print("\n\033[4;31mVOCÊ PERDEU! QUE AZAR\033[0;0m")
                vitoriasMaquina += 1
            else:
                sleep(0.3)
                print(f'''SUA ESCOLHA:
                {papel}''')
                print(f'''ESCOLHA DA MAQUINA:
                {pedra}''')
                print("\n\033[4;32mVOCÊ GANHOU! PARECE QUE VOCÊ ESTÁ COM SORTE\033[0;0m")
                vitoriasJogador += 1

        if escolha in "TE": #If para Tesoura
            sleep(0.6)
            print("\n\033[4;93mPEDRA", end=" ")
            sleep(0.7)
            print("PAPEL", end=" ")
            sleep(0.7)
            print("TESOOOOU", end="")
            sleep(1)
            print("RA\n\033[0;0m")
            if maquina == 1:
                sleep(0.3)
                print(f'''SUA ESCOLHA:
                {tesoura}''')
                print(f'''ESCOLHA DA MAQUINA:
                {tesoura}''')
                print("\n\033[4;36mDESSA VEZ FOI EMPATE!\033[0;0m")
            elif maquina == 2:
                sleep(0.3)
                print(f'''SUA ESCOLHA:
                {tesoura}''')
                print(f'''ESCOLHA DA MAQUINA:
                {pedra}''')
                print("\n\033[4;31mVOCÊ PERDEU! QUE AZAR\033[0;0m")
                vitoriasMaquina += 1
            else:
                sleep(0.3)
                print(f'''SUA ESCOLHA:
                {tesoura}''')
                print(f'''ESCOLHA DA MAQUINA:
                {papel}''')
                print("\n\033[4;32mVOCÊ GANHOU! PARECE QUE VOCÊ ESTÁ COM SORTE\033[0;0m")
                vitoriasJogador += 1

    saida = str(input("\nGostaria de Jogar novamente: [S/N]")).strip().upper()[0]
    os.system("cls")

print(f'''\n\033[1;36mVOCÊ\033[0;0m GANHOU UM TOTAL DE \033[4m{vitoriasJogador}\033[0;0m RODADAS
SEU \033[1;35mADVERSARIO\033[0;0m GANHOU UM TOTAL DE \033[4m{vitoriasMaquina}\033[0;0m RODADAS''')

print("\nE O GRANDE VENCEDOR É")
sleep(0.3)
if vitoriasMaquina > vitoriasJogador: #If que determina quem sera o vencedor baseado no número de vitorias
  print("...",end="   ")
  sleep(1)
  print("...",end="   ")
  sleep(1)
  print("...")
  sleep(1)
  print("\033[1;4;35mSEU ADVERSARIO, A ADMIRAVEL MAQUINA!!\033[0;0m")
  sleep(0.5)
  print("\nNÃO FIQUE CHATEADO, VOCÊ PODE TENTAR QUANTAS VEZES QUISER")
elif vitoriasJogador > vitoriasMaquina:
  print("...",end="   ")
  sleep(1)
  print("...",end="   ")
  sleep(1)
  print("...")
  sleep(1)
  print("\033[1;4;33mVOCÊ! O JOGADOR MAIS ASTUTO DE TODOS OS TEMPOS!!\033[0;0m")
  print("\nPARABÉNS VOCÊ GANHOU NO JOKENPO, JA PODE COLOCAR EM SEU CURRICULO")
else:
  print("...",end="   ")
  sleep(1)
  print("...",end="   ")
  sleep(1)
  print("...")
  sleep(1)
  print("\033[1;30mHOUVE UM EMPATE... QUE SEM GRAÇA, GOSTARIA DE VER UM DOS 2 PERDENDO...\033[0;0m")
