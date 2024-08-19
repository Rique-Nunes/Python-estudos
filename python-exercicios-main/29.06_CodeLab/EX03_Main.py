from EX03_Pessoa import Pessoa

pessoa = Pessoa(str(input("Digite o Nome: ")), int(input("Digite a idade: ")), float(input("Digite o peso: ")), float(input("Digite a altura: ")))

print(pessoa.dados())
print(pessoa.humor())

pessoa.envelhecer(2)
pessoa.engordar(5)

print(pessoa.dados())
print(pessoa.humor())

pessoa.envelhecer(2)
pessoa.emagrecer(10)

print(pessoa.dados())
print(pessoa.humor())