import mysql.connector
from mysql.connector import Error

print("Rotina para enfiar as drogas de dados")
idprod = input("Id do produto: ")
nomeprod = input("Nome do produto: ")
precoprod = input("Preço do produto: ")
quantoprod = input("Quantidade: ")

concatenou = f"({idprod},'{nomeprod}',{precoprod},{quantoprod})"
comando="""INSERT INTO teste_produtos(idproduto,nomeproduto,preco,quantidade)
                            values
                            """
inserir_produtos = comando + concatenou

try:
    con = mysql.connector.connect(
        host='localhost', database='biblioteca', user='root', password='12012006')

    cursor = con.cursor()
    cursor.execute(inserir_produtos)
    con.commit()
    print(cursor.rowcount, "Registros inseridos na tabela")
except Error as erro:
    print('falha ao inserir dados no sql: {}'.format(erro))

finally:
    if (con.is_connected):
        cursor.close()
        con.close()
        print("conexão finalizada")
