# Fazer o método sacar(), se o saldo for menor ou igual a 0, retorne uma mensagem dizendo que o saldo é insuficiente, caso o contrário, realize a operação de saque e mostre o saldo atual dessa conta;

from EX01_Conta import Conta

if __name__ == "__main__":
#     banco = list()

#     while True:
#         conta = Conta(str(input("Nome: ")), float(input("Saldo: ")))
#         banco.append(conta)

#         saida = input("Deseja continuar? [S/N]").upper().strip()[0]
#         if saida == "N":
#             break

# for i in range(len(banco)):
#     print(banco[i].depositar(float(input(f"{banco[i].titular} quanto você deseja depositar? R$"))))
#     print(banco[i].sacar(float(input(f"{banco[i].titular} quanto você deseja sacar? R$"))))
#     print(banco[i].depositar(float(input(f"{banco[i].titular} quanto você deseja depositar? R$"))))


# for o in banco:
#     print(o)

    conta001 = Conta('Pedro', 100)

    conta001.titular = "Gustavo"
    conta001.saldo = 500
    print(conta001)