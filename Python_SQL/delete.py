# Importamos a biblioteca:
import mysql.connector


# Abrimos uma conexão com o banco de dados:
conexao = mysql.connector.connect(host='localhost', database='db_escola', user='root', password='')

# Cria um cursor:
cursor = conexao.cursor()

# Executa o comando:
cursor.execute("DELETE FROM alunos WHERE nome = 'joaquim'")

# Efetua um commit no banco de dados.
# Por padrão, não é efetuado commit automaticamente. Você deve commitar para salvar
# suas alterações.
conexao.commit()

# Finaliza a conexão
conexao.close()
