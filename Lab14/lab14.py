def set_matriz(n):
    """Função para definição da matriz de entrada
    Recebe todas as suas entradas numa lista que as separa para as entradas individuais """

    matriz = []
    for i in range(n):
        linha = input().split()
        aux = []
        for i in linha:
            aux.append(int(i))
        matriz.append(aux)
    return matriz


def exclui_linha(mat, i):
    '''Função para obter a matriz reduzida para os cálculos de LaPlace.
    Exclui a linha e coluna referentes a um valor da matriz.
    Para essa aplicação, sempre se usam valores da primeira linha (que sempre é excluida) e a coluna
    vai se alternando.'''

    aux = []
    for j in range(len(mat)):
        aux1 = []
        for k in range(len(mat[0])):
            aux1.append(mat[j][k])
        aux.append(aux1)
    del aux[0]
    for linha in aux:
        del linha[i]
    return aux


def determinante(matriz):
    """Função recursiva para cálculo de determinantes a partir da expansão de LaPlace"""

    if len(matriz) == 2:
        aux = (matriz[0][0] * matriz[1][1]) - (matriz[0][1] * matriz[1][0])         # Caso base para matrizes 2x2
        return aux
    else:
        soma = 0                                                                    # Somatório dos cofatores
        cont = 0
        for i in range(len(matriz[0])):
            mat1 = exclui_linha(matriz, cont)                                       # Obtenção da matriz reduzida
            A = (-1)**(1 + (cont + 1)) * determinante(mat1)                         # Cálculo do cofator
            soma += A * matriz[0][cont]                                             # Somatório do cofator pelo valor
            cont += 1
        return soma


entrada = int(input())                                              # Número de matrizes a serem calculadas
ordem = int(input())                                                # Ordem das matrizes quadradas
produto = 1                                                         # Variável para o produtório dos determinantes
for i in range(entrada):
    obj = set_matriz(ordem)
    det = determinante(obj)
    produto *= det
print(f'''Após as {entrada} transformações, o objeto {ordem}-dimensional teve o volume multiplicado no valor {produto}.''')