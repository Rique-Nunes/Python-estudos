from random import randint

class Lancador:
    def __init__(self):
        self.dado = randint(1,6)
        self.moeda = randint(0,1)
    
    def lancarDado(self):
        return f'O valor do dado é {self.dado}'

    def lancarMoeda(self):
        if self.moeda == 0:
            self.moeda = "Cara"
        else:
            self.moeda = "Coroa"
        return f'O lado da moeda é {self.moeda}'
        