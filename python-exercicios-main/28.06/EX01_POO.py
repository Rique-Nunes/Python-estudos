class Pessoa:
    def __init__(self, nome, idade, peso):
        self.nomePessoa = nome
        self.idadePessoa = idade
        self.pesoPessoa = peso

    def comer(self, calorias):
        if self.idadePessoa > 30 or self.idadePessoa < 30: 
            self.pesoPessoa += calorias * 2

    def malhar(self, calorias):
        self.pesoPessoa -= calorias

    def mostrarDados(self):
        return f'''
    Nome = {self.nomePessoa}
    Idade = {self.idadePessoa} 
    Peso = {self.pesoPessoa} KG
        '''

pessoa1 = Pessoa(str(input("Nome: ")), int(input("Idade: ")), float(input("Peso: ")))
pessoa2 = Pessoa(str(input("Nome: ")), int(input("Idade: ")), float(input("Peso: ")))

print(pessoa1.mostrarDados())
print(pessoa2.mostrarDados())

pessoa2.comer(int(input("Quantas calorias para a pessoa 2: ")))
pessoa1.malhar(int(input("Quantas calorias pessoa 1 perdeu: ")))

print(pessoa1.mostrarDados())
print(pessoa2.mostrarDados())