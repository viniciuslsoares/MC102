exclui = 0                                  # a variável 'exclui' é criada para ser usada posteriormente pelas funções


def contador_serie(list):
    """Função que retorna uma lista onde o primeiro item é o objeto de maior ocorrência e o segundo o número de vezes
    que apareceu.
    O contador somente considera os itens na ordem em que a lista foi colocada no argumento da função.
    Por exemplo: na lista [0, 0, 1, 1, 1, 0, 0] o retorno será [1, 3], pois foi a maior ocorrência em série."""

    x = list
    cont = 1
    resp = [0, 0]
    for i in range(1, len(x)):
        if x[i] == x[(i - 1)]:
            cont += 1
            reg = x[i]
        else:
            cont = 1
            reg = 0
        if cont > resp[1]:
            resp[1] = cont
            resp[0] = reg
    return resp


def contador_unico(list):
    """Função que conta as ocorrências únicas de uma lista.
    Utiliza do método "sort()" para odená-la e poder testar as ocorrências únicas."""

    global exclui                               # a variável 'exclui' indica para o programa qual item excluir
    exclui = list.pop()                         # da lista final dos nomes
    ordem = sorted(list)                        # cria uma lista auxiliar em ordem alfabética para o contador
    cont = 1                                    # o contador inicia em 1 para considerar o primeiro item da lista
    for i in range(1, len(ordem)):              # esse laço compara um item da lista com o seu anterior
        if ordem[i] != ordem[(i - 1)]:          # e adiciona um ao contador caso seja diferente
            cont += 1
    return cont


def corretor(list):
    """A função realiza duas correções na lista:
    Primeiramente troca os espaços das palavras por '_'
    após isso, transforma as letras dos itens em minúsculas com exceção
    das duas primeiras indicadoras (HA por exemplo)."""

    y = []
    for i in list:                          # y passa a ser a lista nova
        aux = i.replace(' ', '-')           # troca os espaços por '-' nos nomes
        y.append(aux)                       # cria uma lista com os nomes corrigidos

    x = []
    for i in y:                             # x passa a ser a lista nova
        aux1 = i.split('_')                 # em cada item, separa o indicador (HA por ex) do nome
        aux1[1] = aux1[1].lower()           # deixa em letra minúscula o nome
        z = aux1[0] + '_' + aux1[1]         # junta o indicador do nome corrigido
        x.append(z)
    return x


def remove_unico(list):
    """A partir da variável global 'exclui' criada na função 'contador_unico(),
    essa função reconhece qual item excluir da lista de nomes e, através de um laço
    utiulizando o metodo remove() apaga todas as instâncias do ‘item’"""

    global exclui
    x = list
    while exclui in x:
        x.remove(exclui)
    return x


def apaga_copia(list):
    """A função cria uma lista auxiliar somente com os valores únicos
    da lista original, retornando essa lista auxiliar."""

    x = []
    for i in range(len(list)):
        if i == 0:
            x.append(list[i])
        elif list[i] not in x:
            x.append(list[i])
    return x


if __name__ == '__main__':

    lista = input()                             # recebe a lista

    aux = lista.split('/ ')                     # as próximas linhas manipulam a lista original, trocando o indicador '/'
    x = aux[0].split(', ')                      # do último item para uma vírgula e, ao usar o split(', '), retira
    x.append(aux[1])                            # o espaço extra no começo de cada nome
    lista = x

    print(*contador_serie(lista))               # chama a função que indica a maior ocorrência em série de algum item
    lista = corretor(lista)                     # realiza as correções de espaço e caixa alta da lista
    print(contador_unico(lista))                # chama a função que conta os objetos únicos da lista
    lista = remove_unico(lista)                 # chama a função que remove o objeto 'exclui'
    lista = apaga_copia(lista)                  # chama a função que apaga os objetos repetidos

    cc = []                                     # as três próximas listas são para a separação dos indicadores
    ha = []                                     # dos objetos, separando o 'CC', 'HA' e 'CR' em três listas diferentes
    cr = []                                     # e, por fim as printando
    for i in lista:
        if 'CC' in i:
            cc.append(i)
        elif 'HA' in i:
            ha.append(i)
        elif 'CR' in i:
            cr.append(i)
    print(ha)
    print(cr)
    print(cc)
