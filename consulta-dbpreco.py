#!/usr/bin/python
# __autor__ == '__Ivanoel__'

import sqlite3

conexao = sqlite3.connect("preços.db")

cursor = conexao.cursor()


# O comando select utiliza lista de campos e lista de tabelas.
# A palavra from eh utilizada para separar a lista de campos da lista de tabelas.
cursor.execute("select * from preços")

# o método fetchone() retorna a tupla com os resultados de
# nossa consulta ou None, caso a tabela esteja vazia.
resultado = cursor.fetchone()


# Usamos uma string em python e uma máscara com dois %s, um para cada campo
# Assim, resultado[0] eh o primeiro campo, no caso (nome) e
# resultado[1] eh o segundo, (telefone).
print("Nome: %s\nPreços: %s" %(resultado))

# fechamos a conexao com o banco de dados.
cursor.close()
conexao.close()
