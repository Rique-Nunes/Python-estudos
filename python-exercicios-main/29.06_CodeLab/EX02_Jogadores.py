class Jogador:
    def __init__(self, nome, partidas, gols):
        self.nome = nome
        self.golsT = gols
        self.partidas = partidas
    
    def aproveitamento(self):
        return f'''
    Nome: {self.nome}
    Partidas: {self.partidas}
    Gols Total: {self.golsT}
    Aproveitamento: {self.golsT/self.partidas:.2f}
        '''