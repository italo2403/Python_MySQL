import mysql.connector

conexao = mysql.connector.connect(host='localhost', database='db_escola', user='root', password='')

if conexao.is_connected():
    print('Banco Conectado com Sucesso')
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM alunos;')

    for r in cursor.fetchall():
        print(r)

    cursor.close()
    conexao.commit()
    conexao.close()
