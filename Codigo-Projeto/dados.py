#Parte do programa para enviar dados mineirados para banco de dados e suas tabelas
from log_codevasf import datafr

#Importanto Banco de dados
import sqlite3

#Lista para armazenar os dados separadamente
produtos = []
usuarios = []
estacao = []

'''Lista criada para armazenar dados dos produtos após o tratamento das strings no caso retirada de
caracteres especiais '''
produto_fin = []


#Criando conexão com o banco de dados
conexao = sqlite3.connect('log-codevasf-novo.db')

# Cria variavel cursor para executar comando SQL
cursor = conexao.cursor()



for i in datafr:
    produtos.append(i[1])
    usuarios.append(i[2])
    estacao.append(i[3])

for i in produtos:
    val = i.replace('"', '')
    produto_fin.append(val)

#Função Zip faz a iteração de cada linha de uma lista 
registro = zip(produto_fin, usuarios, estacao)


# Variavél criada para armazenar comandos SQL 
sql = 'INSERT INTO codevasf (produto, usuario, estacao) VALUES (?, ?, ?)'

#Função executemany executa o comando sql ate o final da ultima linha da lista sem a necessidade de loop
cursor.executemany(sql, registro)
    
#Salva dados no banco 
conexao.commit()
print ('Dados Salvos com Sucesso !')

#Encerra a conexão com o banco
conexao.close()
print('Programa encerrado com sucesso')
