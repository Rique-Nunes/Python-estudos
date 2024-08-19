# Orientação a objetos: Paradigma de programação
# Classes e Objetos

class Veiculo:
    '''Classe do veiculo'''
    def movimentar(self):
        print(f'Sou um veiculo e me desloco')

    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro = None
    # Setter

    def set_num_registro(self, registro):
        self.__num_registro = registro

    # Getter tras o objeto de dentro da classe e privado para fora
    def get_fabr_modelo(self):
        print(f'Modelo: {self.__modelo}, Fabricante: {self.__modelo}')

    def get_num_registro(self):
        return self.__num_registro


class Carro(Veiculo):
    '''carro baseado na classe veiculo'''
    # Método __init__ será herdado
    def movimentar(self):
        print(f'Sou um carro e ando pelas ruas')


class Motocicleta(Veiculo):
    '''moto baseado na classe veiculo'''
    # o movimentar é polimorfizado ou seja para cada class faz uma coisa
    def movimentar(self):
        print(f'Corro Muito!')


class Aviao(Veiculo):
    '''aviao baseado na classe veiculo'''
    def __init__(self, fabricante, modelo, categoria):
        self.__cat = categoria
        super().__init__(fabricante, modelo)
    # retorna a 'categoria' caracterisitca unica do aviao
    # def get_categoria(self):
    #    return self.__cat

    def movimentar(self):
        print(f'Eu voo alto!')
    # a mesma função usa o super() para indicar as mesmas coisas da função
    # da classe mãe e adiciona o produto interno 'categoria' ambas fazem a mesma função

    def get_fabr_modelo(self):
        super().get_fabr_modelo()
        print(f'categoria: {self.__cat}')


if __name__ == '__main__':
    # meu_veiculo = Veiculo('GM', 'Cadillac')
    # meu_veiculo.movimentar()
    # meu_veiculo.get_fabr_modelo()
    # meu_veiculo.set_num_registro(4903)
    # print(f'Registro: {meu_veiculo.get_num_registro()}')

    # meu_carro = Carro('Volkswagen', 'Polo')
    # meu_carro.movimentar()
    # meu_carro.get_fabr_modelo()

    # seu_carro = Carro('Audi', 'A5 Sport')
    # seu_carro.movimentar()
    # seu_carro.get_fabr_modelo()

    # moto = Motocicleta('Harley', 'Hudson')
    # moto.get_fabr_modelo()
    # moto.movimentar()
    meu_aviao = Aviao('Boeing', 474, 'Comercial')
    meu_aviao.movimentar()
    meu_aviao.get_fabr_modelo()
    # print(f'A Categoria é {meu_aviao.get_categoria()}')
