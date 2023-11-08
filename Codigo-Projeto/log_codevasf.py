#progrma para mineirar dados de um arquivo TXT



# Listas Criadas para armazenar os dados após cada tratamento e especificação dos dados que serão salvo no BD
dados = []
dados_atualizados = []
dados_separados = []
dados_finais = []
dados_alterados = []
codevasf = []

#definindo uma função para abrir o arquivo
def ler_arquivo_txt(caminho_arquivo):
    #Comanando para abertura do arquivo para leitura dos dadso
    with open (caminho_arquivo, 'r') as arquivo:
        # Laço for criado para percorrer cada linha do arquivo e buscar somente dados com 'OUT' e excluir dados com 'AECCOL'
        # Em seguida enviar os dados para uma lista.
        for i in arquivo:
            if 'OUT' in i:
                if 'AECCOL' not in i:
                    #Tratamento dos dados para enviar a lista somente os dados a partir da casa decimal que representa os dados que serão uteis.
                    dados.append(i[24::])
        # Laço for para enviar os dados para uma lista nova para um novo tratamento dos dados
        for val in dados:
            dados_atualizados.append(val)

#Funçao criada para ordenar os dados e remover dados duplicados com o comando set na lista 'dados_atualizado'
def ordena_dados():
    ler_arquivo_txt('debug.log')
    meu_set = set(dados_atualizados)
    usuarios = len(meu_set)

    for valores in meu_set:
        codevasf.append(valores)
        
        
    print(usuarios)



#Função criada para chamar as demais como um efeito dominó
#apos a demais funçoes executadas essa função tem a finalidades de finalizar o tratamento dos dados 
#Separando e removendo caracteres especiais conforme solicitado finalizando toda busca e separação dos dados 
def dados_compilados():
    ordena_dados()

    for i in codevasf:
        valor = i.replace('@', ' ')
        dados_alterados.append(valor)
    
    for i in dados_alterados:
        valor = i.split(' ')
        dados_separados.append(valor)
    
    return dados_separados
    


#Por fim criou-se uma variavel para armazenar a função final para que seja possivel utilizar todo o codigo 
#Em outro codigo para aplicação dos dados em um BD 
#Vale ressaltar que esse código foi criado especificamente para um arquivo txt sendo necessario modificações 
#posteriores caso haja necessidade de abrir um outro arquivo com dados diferentes.
datafr = dados_compilados()




