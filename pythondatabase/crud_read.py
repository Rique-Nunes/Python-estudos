import mysql.connector
from mysql.connector import Error
try:
    con = mysql.connector.connect(
        host='localhost', database='biblioteca', user='root', password='12012006')

    consulta_sql = "select * from teste_produtos"
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    print("Foram retornados tantos dados: ", cursor.rowcount)

    print("\nMostrando os dados: ")
    for linha in linhas:
        print('Idproduto: ', linha[0])  # type: ignore
        print('Nomeproduto: ', linha[1])  # type: ignore
        print('preço: ', linha[2])  # type: ignore
        print('quantidade: ', linha[3], "\n")   # type: ignore
except Error as erro:
    print("Erro ao realizar a operação: ", erro)

finally:
    if (con.is_connected):
        con.close()
        cursor.close()
        print("conexão encerrada")
