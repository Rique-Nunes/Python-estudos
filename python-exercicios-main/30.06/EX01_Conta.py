class Conta:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        return f'''Você depositou {valor:.2f} na conta de {self.__titular}
Seu saldo atual é: R${self.__saldo:.2f}'''


    def __pode_sacar(self, valor_saque):
        return self.__saldo > valor_saque

    def sacar(self, valor):
        if valor > 0:
            if self.__pode_sacar(valor):
                self.__saldo -= valor
                print(f'{self.__titular} você sacou R$ {valor:.2f} com sucesso!')
            else:
                print(f'{self.__titular} você nao tem R$ {valor:.2f} para sacar.')
        else:
            print('Você não pode sacar um valor negativo a da sua conta')
    
    def __str__(self):
        return f'''
        Titular: {self.__titular}
        Saldo: R${self.__saldo:.2f}
        '''

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, titular):
        self.__titular = titular