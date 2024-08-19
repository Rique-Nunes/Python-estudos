# Strings são listas invariavels porem pode variar o conteudo da variavel
# nome = 'Curso de Python'
# aluno = 'rique'
# letra = nome[3]
# print(letra)
# print(len(nome))
# print(nome + ' com ' + aluno)
# frase = 'Vamos aprender python hoje'
# palavras = frase.split()
# print(palavras[1])
# for letra in frase:
#     print(letra)
# print(frase[6:15]) slincing começo:fim

# email = input('digite o seu e-mail')
# arroba = email.find('@')
# print(arroba)
# usuario = email[0:arroba]
# dominio = email[arroba+1:]
# print(usuario)
# print(dominio)

# produtos = 'carbonato de sódio e óxido de zinco'
# print('sódio' in produtos)
# print('magnésio' not in produtos)

# item = 'hipoclorito'
# pos = item.find('clor')
# print(pos)
# pos = item.find('flu')
# print(pos)

# objeto_celeste = 'galáxia espiral M31'
# print(objeto_celeste.upper())
# print(objeto_celeste.lower())
# print(objeto_celeste.title())
# print(objeto_celeste.capitalize())

# frase = '     Omega 3 da topterme é deveras bom   '
# print(frase)
# print(frase.lstrip())
# print(frase.rstrip())
# print(frase.strip())

# fruta = 'Abacate'
# print(fruta)
# print(fruta.rjust(20))
# print(fruta.center(20))
# print(fruta.ljust(20, '-'))

# p = 'Boson Treinamentos'
# print(p.startswith('B'))
# print(p.endswith('s'))

# Docstrings
texto = """
Docstring é uma espécie de documentação que podemos iserir dentro de um
módulo, funções ou classes no python, entre outros locais.
    respeita desloamento do texto e é multilhinhas
"""
print(texto)
