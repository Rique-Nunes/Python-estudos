# DESAFIO - Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mes Por Extenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida. Considere que Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, sendo que nesses casos Fevereiro terá 29 dias.



mes= {1: 'janeiro', 2 : 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio'}
ano = {2000: 'dois',3: 'três' , 4:'quatro' , 5:'cinco' , 6:'seis' , 7: 'sete' , 8: 'oito' , 9: 'nova' , 10: 'dez'}
aniver = '21/03/1976'
dia, mes, ano = aniver.split("/")
print (f'Data nascimento: %s/%s/%s' % (dia, mes[int(mes)], ano[int(ano)]))