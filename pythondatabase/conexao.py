import mysql.connector

con = mysql.connector.connect(
    host='localhost', database='biblioteca', user='root', password='12012006')

if con.is_connected():
    db_info = con.get_server_info()
    print('conectado ao servidor mysql versão ', db_info)
    cursor = con.cursor()
    cursor.execute('select database();')
    linha = cursor.fetchone()
    print('Conectado a banco de dados ', linha)

if con.is_connected():
    cursor.close()
    con.close()
    print('conexão foi encerrada')

