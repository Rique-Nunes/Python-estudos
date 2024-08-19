#Crie uma classe chamada Conta para simular as operações de uma conta corrente. Sua classe deverá ter os atributos Titular e Saldo, e os métodos Sacar e Depositar. Crie um objeto da classe Conta e teste os atributos e métodos implementados.​ Adicione uma regra no método Sacar, onde o usuário só poderá sacar se o Saldo for maior que zero, caso contrário mostre a mensagem na tela: "Você não tem saldo suficiente para essa operação."

class Conta:
    def __init__(self, titular, saldo):
        self.titularConta = titular
        self.saldoConta = saldo
    
    def Sacar(self, saque):
        if self.saldoConta > 0:
            self.saldoConta -= saque
            return f'Você sacou {saque}'
        else:
            return f"\nVocê não tem saldo suficiente para essa operação."

    def Depositar(self, deposito):
        self.saldoConta += deposito
        return f'Você depositou {deposito}'

    def mostrarDados(self):
        return f'''
        Titular = {self.titularConta}
        Saldo = R${self.saldoConta}
        '''

cliente = Conta(str(input("Titular: ")), float(input("Saldo: ")))

print(cliente.mostrarDados())

print(cliente.Sacar(float(input("Quanto deseja sacar: "))))

print(cliente.mostrarDados())

print(cliente.Depositar(float(input("Deseja depositar quanto: "))))

print(cliente.mostrarDados())

print(cliente.Sacar(float(input("Quanto deseja sacar: "))))

print(cliente.mostrarDados())

