# importando sqlite3
import sqlite3 as lite

# criando e conectando com o banco de dados
con = lite.connect('todo.db')
# Criar tabela
# with con:
#    cur = con.cursor()
#    cur.execute( "CREATE TABLE tarefa(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")