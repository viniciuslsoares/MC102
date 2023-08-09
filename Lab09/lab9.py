def cria_matriz(n, m, valor=0):
    """Código retirado dos slides de aula (professor autozia o uso de código disponibilizado por ele)
    Cria uma matriz de dimensões n e m com entradas padrões em zero para as funções de espelhamento e rotação """

    matriz = []
    for i in range(n):
        matriz.append([])
        for j in range(m):
            matriz[i].append(valor)
    return matriz


def set_matriz(n, m):
    """Função para definição da matriz 'imagem' de entrada
    Recebe todas as suas entradas numa lista que as separa para as entradas individuais """

    matriz = []
    for i in range(n):
        linha = input().split()
        for j in range(m):
            linha[j] = linha[j]
        matriz.append(linha)
    return matriz


def transf_normal(pc, pl, l, h):
    """Função para selecionar uma área da imagem e copiá-la em uma matriz auxiliar"""

    global imagem                   # entrada do tipo p coluna, p linha, largura, altura
    selec = []
    for i in range(pl, pl + h):
        linha = []
        for j in range(pc, pc + l):
            linha.append(imagem[i][j])
        selec.append(linha)
    return selec


def transf_apaga(pc, pl, l, h):  # joga uma parte da imagem para uma área de transferência
    """Análoga à função transf_normal, porém, 'apaga' a área selecionada
    trocando os seus valores por '000'"""

    global imagem
    selec = []
    for i in range(pl, pl + h):
        linha = []
        for j in range(pc, pc + l):
            linha.append(imagem[i][j])
            imagem[i][j] = '000'
        selec.append(linha)
    return selec


def print_matriz(matriz):
    """Função para imprimir a matriz, com cada uma de suas linhas em uma
    nova linha e usando o operador '*' para excluir as marcas da lista"""

    for i in range(len(matriz)):
        print(*matriz[i])


def cola(pc, pl):
    """Baseado no ponto de entrada, substitui os valores da imagem pelos
    valores armazenados na matriz auxiliar"""

    global imagem, selec
    for linha in selec:
        for i in range(len(selec)):
            for j in range(len(selec[0])):
                imagem[i + pl][j + pc] = selec[i][j]
    return


def espelho_h(matriz):
    """Usando uma matriz vazia como base, reorganiza os valores da imagem original
    espelhando-os com base num eixo vertical"""

    n, m = len(matriz), len(matriz[0])
    roda = cria_matriz(n, m)
    for i in range(n):
        linha = matriz[i]
        for j in range(m):
            roda[i][-(1 + j)] = linha[j]
    return roda


def espelho_v(matriz):
    """Usando uma matriz vazia como base, reorganiza os valores da imagem original
    espelhando-os com base num eixo horizontal"""

    n, m = len(matriz), len(matriz[0])
    roda = cria_matriz(n, m)
    for i in range(n):
        linha = matriz[i]
        for j in range(m):
            roda[-(1 + i)][j] = linha[j]
    return roda


def rotacao_d(matriz):
    """Usando uma matriz vazia como base, reorganiza os valores da imagem original
    rotacioonando 90° para a direita"""

    n, m = len(matriz), len(matriz[0])
    roda = cria_matriz(m, n)
    cont = 0
    for item in matriz:
        for j in range(m):
            roda[j][-(cont + 1)] = item[j]
        cont += 1
    return roda


def zera_selec():
    """Transforma todas as entradas da matriz 'selec' auxiliar
    em '000'"""

    global selec
    n, m = len(selec), len(selec[0])
    for i in range(n):
        for j in range(m):
            selec[i][j] = "000"
    return


entrada = input().split()                               # Recebe o input de dimensões da matriz
m, n = int(entrada[0]), int(entrada[1])
op = int(input())                                       # Define o número de operações a ser realizado
imagem = set_matriz(n, m)                               # Recebe os valores da imagem a ser editada
selec = []                                              # Cria a matriz auxiliar vazia
Pc = 0                                                  # O ponto Pc representa o ponto da coluna da seleção atual
Pl = 0                                                  # O ponto Pl representa o ponto da linha da seleção atual
l = 0                                                   # Cria as variáveis de largura e altura para a seleção
h = 0

for loop in range(op):                                  # Inicia o loop de operações
    comand = input().split()                            # Recebe o comando a ser executado
    if comand[0] == 'rotacao':                          # Comando de rotação
        if not selec:                                   # Ao longo do programa, testa se a matriz a
            imagem = rotacao_d(imagem)                  # ser alterada é imagem toda ou uma seleção
        else:
            selec = transf_apaga(Pc, Pl, l, h)          # Para caso a matriz seja retangular e a matriz rotacionada
            selec = rotacao_d(selec)                    # não tenha as dimensões da orignal, deixa toda a área selec
            cola(Pc, Pl)                                # em zeros e cola a nova rotacionada em cima, sobrepondo
    elif comand[0] == 'selecao':                        # um pouco da imagem e deixando zeros onde antes estava
        Pc, Pl, l, h = int(comand[1]), int(comand[2]), int(comand[3]), int(comand[4])       # Comando de selecao
        selec = transf_normal(Pc, Pl, l, h)             # Guardas as coordenadas da seleção e a matriz auxiliar
    elif comand[0] == 'recorte':                        # Função recorte
        selec = transf_apaga(Pc, Pl, l, h)              # Apaga a área onde a seleção estava
        pc, pl = int(comand[1]), int(comand[2])         # Define o ponto onde irá ser colada
        cola(pc, pl)                                    # Cola a imagem selecionada
        zera_selec()                                    # Apaga a matriz auxiliar pois a área de seleção está zerada
    elif comand[0] == 'copia':                          # Função cópia
        selec = transf_normal(Pc, Pl, l, h)             # Copia novamente a área selecionada pelos pontos Pc e Pl
        pc, pl = int(comand[1]), int(comand[2])         # Define as coordenadas onde será colada
        cola(pc, pl)                                    # Cola a imagem selecionada
    elif comand[0] == 'espelhamento' and comand[1] == 'h':      # Função de espelhamento horizontal
        if not selec:
            imagem = espelho_h(imagem)                  # Testa para ver se é numa região ou na imagem toda
        else:
            selec = transf_normal(Pc, Pl, l, h)         # Copia a área a ser espelhada
            selec = espelho_h(selec)                    # Espelha a matriz auxiliar
            cola(Pc, Pl)                                # Cola no ponto original
    elif comand[0] == 'espelhamento' and comand[1] == 'v':      # Função de espelhamento vertical
        if not selec:
            imagem = espelho_v(imagem)
        else:                                           # Análogo ao horizontal
            selec = transf_normal(Pc, Pl, l, h)
            selec = espelho_v(selec)
            cola(Pc, Pl)
print_matriz(imagem)                                    # Devolve a matriz imagem final
