#!/usr/bin/python3
# __autor__ == '__Ivanoel__'

# Banco de Dados SQLite, tem varias funções e objetos que acessam o banco.
import sqlite3

# criamos o .db
conexao = sqlite3.connect('preços.db')
 
# cursores são objetos utilizados para enviar comandos e
# receber resultados do db chamando o método cursor().
cur = conexao.cursor()



# vamos criar uma tabela chamada preços o comando usando do sql eh create.
cur.execute('''create table preços(
               nomeP text,
               precoP text)
            ''')

# o método execute enviar o comando ao banco de dados (db).
# o comando insert precisa da tabela onde vai ser inseridos os dados e
# tbm do nome do campos respectivos valores.
# (into) faz parte do comando insert, eh escrito antes da tabela.
# Os valores que vamos inserir na tabela sao especificos tbm entre parenteses
# na segunda parte do comando insert que começa apos a palavra (values).


cur.execute('''
            insert into preços(nomeP, precoP)
            values(?, ?)
            ''', ("Arroz", "4.50"))
# irão substituir as interrogações qndo for executado



# commit eh uma opração que modificar o db.
conexao.commit()

# (close) fechamos cursor e conexao com o db.
cur.close() 
conexao.close()
