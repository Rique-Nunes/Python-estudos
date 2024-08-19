from time import sleep

print('''                                                                                                  
                                  .oys:                                                             
                                  dMMMMs:/+++:`                                                     
                               `+dMMMMMMMMMMMMNdo:`                                                 
                              -mMMMMMMMMMMMMMMMMMMNy+.                                              
                             :NMMMMMMMMMMMMMMMMMMMMMMNh:                                            
                            .NMMMMMMMMMMMMMMMMMMMMMMMMMMh.                                          
                            yMMMMMMMMMMMMMMMMMMMMMMMMMMMMN/                                         
                           /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMyoo++:-`                                 
                           mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmo`                               
                          -MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo                               
                          /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMms`                               
                          oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmhyo/-.                                 
                         `hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh.                                      
                       .+dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm:                                     
                     `omMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs`                                   OLÁ TUDO BEM?
                     sNNNmmyohMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy                                   PODE SE SENTAR, GOSTARIAMOS DE FAZER UMAS PERGUNTAS PRA VOCÊ
                     ---.`   `NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMhoso:                                   ESPERAMOS QUE COOPERE CONOSCO.
                              +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMs                                       
                              .MMMMMMMMMMMMMMMMMMMMMMMMMMMMM+                                       
                              oMMMMMMMMMMMMMMMMMMMMMMMMMMMMm`                                       
                           :+yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm                                        
                          oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM:     -.``                              
                         sMMMMMMMMMMMMMMMMMMMMMMMMMdhdmNMMNs`     yddmdy+.        .`                
                       -dMMMMMMMMMMMMMMMMMMMMMMMMMm                   .+mMm:     hMNo/-.            
                     -yMMMMMMMMMMMMMMMMMMMMMMMMMMN-                     `mMM/   /MMMMMMMMmh-        
                  `+dMMMMMMMMMMMMMMMMMMMMMMMMMMMh`                       /MMN.  dMMMMMMMMMM-        
                -yNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh-                      `MMMm-.MMMMMMMMMMM+        
              -hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/                      dMMMMmMMMMMMMMMMMy        
            `yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm                      :MMMMMMMMMMMMMMMMh        
           .mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM-                      /NMMMMMMMMMMMMMM:        
          `mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo                       `oMMMMMMMMMMMMs         
          /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo                         dMMMMMMMMMMd`         
          dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs                         .NMMMMMMMMM-          
         -MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN.                         /MMMMMMMMs           
         yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm.                       .oMMMMMMMM`           
        .NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd.                    :hNMMMMMMMMd            
        oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm-                 .yNMMMMMMMMMMh            
       `mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN/`             `oNMMMMMMMMMMMMd            BOM, VAMOS LÁ
       /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh-      `..-./mMMMMMMMMMMMMMMN`           
       dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN+--:+ydmNMNMMMMMMMMMMMMMMMMM:           
      -MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh           
      yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.          
     `NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.          
     :MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+           
     sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN/            
     dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN:             
    `MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd.              
    :MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh`               
    :ysssyysssysssyyssyysssyyssyysssyyssyysssysssyysssysssyyssyysssyyssyysssyyssyyo                 
                                                                                                    \n''')
                                                                                                    
sleep(1)

p1 = (input("\nVocê fez algum telefonema para a vítima? [S/N]")).strip().upper()[0]
if p1 == "S":
  p1 = 1
elif p1 == "N":
  p1 = 0
else:
  print("Responda corretamente por gentileza!")
  p1 = -1

print("Entendo...")
sleep(1.5)
print("Oque é isso? Não se preocupe, estou apenas fazendo algumas anotações")
sleep(1) 

p2 = (input("\nVocê esteve no local onde ocorreu o crime? [S/N]")).strip().upper()[0]
if p2 == "S":
  p2 = 1
elif p2 == "N":
  p2 = 0
else:
  print("Responda corretamente por gentileza!")
  p2 = -1

print("Certo...")
print("Vamos prosseguir")
sleep(1)

p3 = (input("\nVocê mora proximo da vítima? [S/N]")).strip().upper()[0]
if p3 == "S":
  p3 = 1
elif p3 == "N":
  p3 = 0
else:
  print("Responda corretamente por gentileza!")
  p3 = -1
sleep(1)

p4 = (input("\nVocê devia alguma coisa para a vítima? [S/N]")).strip().upper()[0]
if p4 == "S":
  p4 = 1
elif p4 == "N":
  p4 = 0
else:
  print("Responda corretamente por gentileza!")
  p4 = -1
sleep(1)
print("Vamos a ultima pergunta, agradecemos sua colaboração")
sleep(1)

p5 = (input("\nVocê já trabalhou com ou para a vítima? [S/N]")).strip().upper()[0]
if p5 == "S":
  p5 = 1
elif p5 == "N":
  p5 = 0
else:
  print("Responda corretamente por gentileza!")
  p5 = -1
print("OK...")

resposta = p1+p2+p3+p4+p5

sleep(3)

if resposta == 2 or resposta == 1:
  print('''                                          `--+syydmmNMmdmmmNmhyo/                                             
                                        `:+oNMMMMMMMMMMMMMMMMMMMMd.                                           
                                      `+mNMMMMMMMMMMMMMMMMMMMMMMMMN:                                          
                                     `hMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+                                         
                                   `oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs                                        
                                  .dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy                                       
                                  hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs                                      
                                  sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+-.`                                  
                                  +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMsssyysso+/:-.`                        
                                  /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo  ```...-:/+oo+:                     
                                  -MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/              ``                     
                                  .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh:                                    
                                   mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo`                                  
                                 -ommMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh.                                 BOM, OBRIGADO PELA COLABORAÇÃO,
                              `:yho-`oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm-                                APÓS A NOSSA ANALISE DECLARAMOS QUE VC SE ENQUADRA NO 
                             :ys-`    yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdddh/                                                  
                           -so-       sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd``                                                         \033[1;4;33m[SUSPEITO]\033[0;37m
                          /+.       `sNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN/.                                   
                                  `/mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMyyys:                                POR FAVOR PERMANEÇA AQUI, PRECISAMOS FAZER UMA NOVA INVESTIGAÇÃO
                                 -hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs  -sN:                               
                               `sNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh    dd                               
                             `/mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN.   dM-                              
                            -hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNsoydmNNNNNNm/   `MMo   /yso/.`                    
                          `sNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMms/  `.-----`    .MMd  .MMMMMMmh:                  
                         -mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd.              `MMM/ -MMMMMMMM/                  
                        /NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd`                mMMN/yMMMMMMN/                   
                       oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd:                :NMMMMMMMMMM/                    
                     `yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs`               :mMMMMMMMN/                     
                    .dMMmyssssyhmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMd.                :ohmNdo.                      
                   :NMy-          `-:+shmMMMMMMMMMMMMMMMMMMMMMMN:                                             
                  -yo.                   `-+shmMMMMMMMMMMMMMMMNNm/                                            
                                               `.://////::-..`                                                ''')
elif resposta == 3 or resposta == 4:
   print('''
                              +mMNdysoosyhhhyyo/-`                                                          
                           .+dMMMMMMMMMMMMMMMMMMMNh+.                                                       
                         -yNMMMMMMMMMMMMMMMMMMMMMMMMNd+.                                                    
                       .yNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNh/`                                                 
                      +NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNy/.                                              
                    `yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN:`                                            
                   `yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmy/.                                         
                   sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNds/-`                                    
                  .NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNms                                   
                  -MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdyo:`                                   
                  `mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd/-..`                                       
                   sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd                                            
                   /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy                                            
                   oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNs:`                                         
                   +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMds:`                                      
                   .NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd+                                     
                  .oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmds                                     
               .:yNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs:.`                                       
            .+hmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.                                          
           `yNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh-                                          CONFORME NOSSA SUAS RESPOSTA A NOSSA ANALISE 
             .:/+oossssNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNhhyso/.                                     CONFIRMOU QUE VOCÊ SE ENQUANDRA NO PERFIL DE
                     :dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo..-/hNy`                                                     
                ``-/yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+     oMd.                                                     \033[4;1;31m[CÚMPLICE]\033[0;37m
              .ymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd      oMm.                                 
              -NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN`      sMh                                  POR FAVOR NOS ACOMPANHE ATÉ SUA CELA
               :mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNddhhy-       `mMy-       -shmmNmdyo.             ONDE VOCÊ DEVERÁ PERMANACER ATÉ O ALVARA DO JUIZ!
                 sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo.              .NMMN.     .hMMMMMMMMMm.            
                +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd.                 :MMMd`      yMMMMMMMM.             
               oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm`                   oMMMh`    .oMMMMMMMd              
              sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNho:`                 yMMMm/` :MMMMMMMMMm+`            
             sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdo:`              oNMMMNddMMMMMMMMMMMN-           
            sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmy:`            ./yMMMMMMMMMMMMMMMMh           
           sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmo.            /MMMMMMMMMMMMMMMMN.          
          oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNy-          `+oomMMMMMMMMMMMMMo          
         :MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNs.          -hMMMMMMMMMMMMMMm`         
        .mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm/        /NMMMMMMMMMMMMMMMMd`        
        -MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNs`      mMMMMMMMMMMMMMMMMMM.        
        -MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh`    .MMMMMMMMMMMMMMMMMMh         
        .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh`   -MMMMMMMMMMMMMMMMMM:         
        .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy  `-MMMMMMMMMMMMMMMMMh          
        .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+`hmMMMMMMMMMMMMMMMMN-          
        `MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNyMMMMMMMMMMMMMMMMMM+           
        `NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN+            
        `NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd`            
        `mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM:            
        `mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy            
         dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm`           
         dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM-           
         hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/           
         hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs           
         hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd           
         yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN           
         sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN.          
         sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM-          ''')
elif resposta == 5:
   print('''                                                   -mmh+.   `sNN-                                             
                                                   `sMNdNh::mNmm`                                             
                                                  `-:oNMMMMMMmN+-.                                            
                                             `:ohNMMMMMMMMMMMMMMMMNdy+:`                                      
                                          .+dMMMMMMMMMMMMMMMMMMMMMMMMMMNdo-                                   
                                        :hNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmo-                                
                                      /dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh/                              
                                    .hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd/                            
                                   +NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd-                          
                                  sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo`                        
                                 sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd.                       
                                oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm-                      
                               :MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN-                     
                              `mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN-                    
                              sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm.                   
                             /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd`                  
                            -NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh`                 
                           :mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm+.               
                         .sNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNy:`            
                       .sNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmy/.         
                    `:yNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNh+-      
                  .+dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNds:`  
                -smMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmNMMMMMMMMMMMMMMMMmy-
             `/hNMMMMMMMMNmhodMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/..-:/+osyhhddmmmmmds
            +mMMMNmdhys+:.`  sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh           ```````` 
            .---...`         /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN.                   
                             .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNs.                    
                              mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm/`                    
                              sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy                    
                              /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/                   
                              `NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh                               COM BASE NA NOSSA ANALISE ENCIMA DA SUAS RESPOSTAS
                               hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN`                              CONFIRMO EM NOME DA LEI QUE SEU PERFIL SE ENQUANDRA COMO
                               /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo                            
                               `NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm`                                                    \033[4;1;31m[CULPADO]\033[0;37m
                       sy/.     yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+                 
                      `MMMmh+.  .dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm                             CONFORME AS LEIS JUDICIAIS EU PEÇO QUE SE RETIRE DO LOCAL JUNTO AOS GUARDAS
                      -MMMMMMNh+-oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmNNNNNmms                             VOCÊ SERA LEVADO PARA O DP MAIS PROXIMO ONDE FICARÁ ATÉ O DIA DO SEU JULGAMENTO!
                      sMMMMMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd.......`                  
                     `NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM-                         
                     oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmho-`                     
                    -NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNy:odMMd/                    
                   `dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd+:`  `+NMMy`                  
                   sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd       oMMMo  `....``         
                  oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+       mMMN`-dNNNmmdhyo/-.   
                 +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNMMMMMMMMMMMMMMMMMN:      oMMMsdMMMMMMMMMMMMNh/ 
                +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo-/odNMMMMMMMMMMMMMm.      -MMMMMMMMMMMMMMMMMMMm 
               oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd+` `:odNMMMMMMMNy.       `mMMMMMMMMMMMMMMMMMMy 
             `yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMms.   .:+ssso/.          +MMMMMMMMMMMMMMMMMN. 
            .hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNy:`                    sMMMMMMMMMMMMMMMM+  
           :mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd/`                   /mMMMMMMMMMMMMN+   
          +NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm+`                  `+hNNMMMMMNms-    
        `sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmo`                   `-/+++/-`      
       `hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo`                                
      .dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm+`                              
     .mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm/`                            
    .mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd-                           
   `dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMysyhdmNNN-                          
   hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo      `                           
  oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd.                                
 -MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN/                               
 dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs                              
:MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh`                            
yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm.                           
NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm`                          
mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN:                          ''')
elif resposta == 0:
   print('''

                                                    -smMMmho-                                                 
                                                  :dMMMMMMMMMNho:`                                            
                                     -:`        -hMMMMMMMMMMMMMMMNh/                                          
                                     mMNs.    :hMMMMMMMMMMMMMMMMMMMMNs.                                       
                                    `MMMMMmhdMMMMMMMMMMMMMMMMMMMMMMMMMMh/`                                    
                                     +dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNh+`                                 
                                       `yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNs`                               
                                       .NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd`                              
                                       dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo                              
                                      /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+                              
                                      hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm                               
                                     -MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM:                               
                                     dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+                                
                                    oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo                                 
                                   +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy                                  
                                  /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm`                                  
                                 /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+                                   
                                +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh`                                    ANALISAMOS O SER PERFIL E VOCÊ SE ENCAIXA NO QUADRO DE 
                               yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNymMMMMm/ -+:                                                   
                             `dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM`  -sNMMMmMMMdmd+.--                                              \033[1;4;32m[INOCENTE]\033[0;37m
                       `:+:.-dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN     `dMMMMMMMMMMMMMdoo:                   
                     `oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN`     .dMMMMMMMMMMMMMMMMNy-               VOCÊ ESTA LIBERADO PARA IR, AGRADECEMOS SUA COOPERAÇÃO CONOSCO!
                    :mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM`      oMMMMMMMMMMMMMMMMMMN`              
                  -yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdss+       `sMMMMMMMMMMMMMMMMMM.              
              `-+hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh`            yMMMMMMMMMMMMMMMMMs              
      `.:/oydNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo-              /MMMMMMMMMMMMMMMMMM/             
+oydmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN/-`                `hMMMMMMMMMMMMMMMMMd             
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMddh/                     :dMMMMMMMMMMMMMMMd             
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmy/.                      .mMMMMMMMMMMMMMMy             
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNho:`                  .dMMMMMMMMMMMMMN.            
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMds:`                ./NMMMMMMMMMMMm.           
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNy.                :NMMMMMMMMMMMo           
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo.               /MMMMMMMMMMMm.          
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNds-            :MMMMMMMMMMMd`         
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs`           +MMMMMMMMMMMd`        
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNhyo+/.      sMMMMMMMMMMMh        
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd-     dMMMMMMMMMMMs       
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN:    -MMMMMMMMMMMMo      
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN:    sMMMMMMMMMMMM:     
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy-  `NMMMMMMMMMMMN.    
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd+`mMMMMMMMMMMMMh    
''')
else:
  print("\ntSUA RESPOSTA NAO SE ENQUADRA NOS REQUISITOS, ESTAMOS UMA INVESTIGAÇÃO POR FAVOR LEVA ISSO MAIS A SÉRIO, CASO AO CONTRARIO TEREMOS QUE MUDAR NOSSA ABORDAGEM!!")