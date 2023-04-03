import mysql.connector

conexao = mysql.connector.connect(host='localhost', database='db_escola', user='root', password='')

if conexao.is_connected():
    print('Banco Conectado com Sucesso')
    cursor = conexao.cursor()

    # Inserir um novo aluno na tabela
    sql_insert = "INSERT INTO alunos (nome) VALUES (%s)"
    alunos = ('Paulo',)
    cursor.execute(sql_insert, alunos)

    conexao.commit()
    cursor.close()
    conexao.close()
