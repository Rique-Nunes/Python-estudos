from random import randint

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.emocao = randint(1,5)

    def envelhecer(self, acrescimo):
        if self.idade + acrescimo < 21:
            self.altura += 0.5
        else:
            self.altura += (21 - self.idade)*0.5
        self.idade += acrescimo

    def engordar(self, peso):
        self.peso += peso
    
    def emagrecer(self, peso):
        self.peso -= peso

    def humor(self):
        self.emocao = randint(1,5)
        if self.emocao == 1:
            self.emocao = "Você está alegre"
        elif self.emocao == 2:
            self.emocao = "Você está Triste"
        elif self.emocao == 3:
            self.emocao = "Você está com raiva"        
        elif self.emocao == 4:
            self.emocao = "Você está com medo"
        elif self.emocao == 5:
            self.emocao = "Você está animado"
        return f'Humor: {self.emocao}'
    
    def dados(self):
        return f'''
Nome: {self.nome}
Idade: {self.idade} anos
Peso: {self.peso}kg
Altura: {self.altura}cm'''