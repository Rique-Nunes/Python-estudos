#Utilizando os conceitos de Orientaçãoa Objetos (OO) vistos na aula anterior,crie um lançador de dados e moedas em que o usuário deve escolher o objeto a ser lançado.Não esqueça que os lançamentos são feitos de forma randômica.

from EX01_Lancador import Lancador

lancarMoeda = Lancador()
lancarDado = Lancador()

escolha = str(input("Deseja lançar Moeda ou Dado? Dado")).strip().upper()[0]

if escolha == "M":
    print(lancarMoeda.lancarMoeda())
elif escolha == "D":
    print(lancarDado.lancarDado())
else:
    print("Escolha inválida")
    