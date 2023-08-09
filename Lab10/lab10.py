from operator import itemgetter


def set_matriz(n):
    """Função para definição da matriz 'imagem' de entrada
    Recebe todas as suas entradas numa lista que as separa para as entradas individuais """

    matriz = []
    for i in range(n):
        linha = list(input())
        matriz.append(linha)
    return matriz


def print_matriz(matriz):
    """Função para imprimir a matriz, com cada uma das suas linhas numa
    nova linha e usando o operador '*' para excluir as marcas da lista"""

    for i in range(len(matriz)):
        print(*matriz[i])


def comparador(dna1, dna2):
    """A fita de DNA consiste em uma matris de duas linhas
    essa função compara a coluna i de uma fita com outra e conta o número de mutações"""

    cont = 0
    for i in range(len(dna1[0])):
        aux1 = dna1[0][i] + dna1[1][i]
        aux2 = dna2[0][i] + dna2[1][i]
        if aux2 > aux1:
            cont += 1
    return cont


def recebe_fita():
    """Função que recebe as informações do DNA e separa em nome, fita e uma variável
    de quantidade que é alterada pelo comparador"""

    dicio = {'nome': input(), 'fita': set_matriz(2), 'qnt': 0}
    return dicio


def recebe_especie():
    """Função que recebe as informações das espécies e separa em nome (índice e nome científico) e suas
    carcterísticas"""

    aux = input().split('|')
    nome = aux[0].split()
    aux1 = {'nome': [int(nome[0]), nome[1] + ' ' + nome[2]], 'carac': aux[1].split()}
    return aux1


entrada = int(input())
especies = []                               # lista que armazena as espécies e usas características
for i in range(entrada):                    # Recebe uma quantidade pré definida de espécies
    aux = recebe_especie()
    especies.append(aux)

lista = []                                  # lista que armazenas as características e suas fitas de dna
entrada = int(input())                      # Recebe as fitas de DNA e compara com a primeira (mais antiga)
for i in range(entrada):
    lista.append(recebe_fita())
for i in range(len(lista)):
    dna0 = lista[0]
    dnan = lista[i]
    aux = comparador(dna0['fita'], dnan['fita'])
    lista[i]['qnt'] = aux
dna = sorted(lista, key=itemgetter('qnt'))              # Ordena as fitas de DNA de acordo com a quantidade
especies = sorted(especies, key=itemgetter('nome'))     # Ordena as espécies de acordo com o nome

mutacoes = []
for i in dna:
    mutacoes.append(i['nome'])                          # Cria uma lista somente com o nome das mutações em ordem

ordem = []
for i in range(len(mutacoes)-1, -1, -1):
    for j in especies:                                  # Retira os animais de acordo com a mutação mais nova
        if mutacoes[i] in j['carac']:
            ordem.append({'carac': mutacoes[i], 'nome': j['nome']})
            j['carac'] = []                             # Limpa as características para evitar espécies repetidas

ordem = sorted(ordem, key=itemgetter('nome'))           # Ordena de acordo com o nome
for item in mutacoes:
    print(f'CARACTERÍSTICA: {item}')                    # Printa cada mutação e as espécies que a possuemx
    for i in ordem:
        if i['carac'] == item:
            print(*i['nome'])
