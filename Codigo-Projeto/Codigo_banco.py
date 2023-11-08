#Criação de banco de dados para amrmazenar dados dos produtos, usuário e estação

#Programa criado com o intuido de salvar dados especificos de um arquivo de log

#importando Banco de dados
import sqlite3

#Criando banco de dados
conexao = sqlite3.connect('Log-codevasf-.db')

#cria um curosr para executar comandos sql
cursor = conexao.cursor()

#Variavel criada para armazenar comando sql
sql = 'CREATE TABLE IF NOT EXISTS codevasf (produto VARCHAR (50), usuario VARCHAR (30), estacao VARCHAR(30))'

#Comando para executar SQL
cursor.execute(sql)

#comando para salvar as alteraçoes na tabela
conexao.commit()

#comando para encerrar a conexão com a tabela
conexao.close()
