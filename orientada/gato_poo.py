"""TESTANDO ORIENTAÇÃO A OBJETOS COM GATOS"""


class Gato:
    """Esse tipo de variável é fixo independende de quantas
    instancias forem requisitadas, porém tem como modificar o tipo_animal
    na classe ou em um objeto especifico
    variaveis do tipo self são variaveis de cada instancia em si"""
    tipo_animal = "felino"

    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self.__coleira = None

    def set_coleira(self, coleira):
        self.__coleira = coleira
        return print("Coleira selecionada com sucesso")

    def get_atributos(self):
        print(f"O nome do gato é {self.__nome} e sua idade é {self.__idade}")

    def get_coleira(self):
        return self.__coleira


nc = str(input('digite o nome do gato: '))
ig = int(input('\nDigite a idade do gato: '))
gat1 = Gato(nc, ig)
gat1.set_coleira(str(input("digite a coleira: ")))
gat1.get_atributos()
print(f"{gat1.get_coleira()}")
