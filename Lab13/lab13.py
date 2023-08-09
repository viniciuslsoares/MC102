def ordenador(arq):
    """Função que organiza e retorna a string formatada do arquivo ou pasta
    com suas instâncias anteriores"""
    global pasta, lista
    if arq['sub'] == pasta:                                     # caso base onde a pasta sub eh o diretório principal
        return pasta + '_' + arq['atual']                       # string formatada
    for j in lista:
        if j['atual'] == arq['sub']:                            # identação para procurar o diretório em que a pasta
            aux1 = j                                            # se encontra
    return ordenador(aux1) + '_' + arq['atual']                 # recursão até chegar ao caso base


entrada = input().split()
n = int(entrada[1])                                             # número de arquivos a serem processados
pasta = entrada[0]                                              # nome do diretório principal
lista = []                                                      # lista com todos os diretórios e arquivos
for i in range(n):                                              # laço para receber os arquivos
    aux = input().split()
    arq = {'sub': aux[1], 'atual': aux[0]}                      # arquivo na forma de dicionário
    lista.append(arq)                                           # adicionar arquivo na lista de pastas
    print(ordenador(arq))                                       # printar o retorno da recursão
