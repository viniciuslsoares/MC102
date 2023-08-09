from datetime import date


def entrada_de_dado(dado):
    """Função para criar um produto a partir de uma lista de características
    Ignorando o operador (1 ou 0) e atribuindo uma chave para cada característica"""

    while len(dado) < 6:
        dado.append('0')
    produto = {'nome': dado[1], 'quant': int(dado[2]), 'cat': dado[3], 'preço': float(dado[4]), 'val': int(dado[5])}
    return produto


def adiciona_estoque(produto):
    """Função para adicionar um produto ao estoque
    Caso seja a primeira adição, cria um ‘item’ na lista estoque
    Caso ja exista algum produto com o mesmo nome, atualiza o preço, quantidade e validade"""

    global estoque
    item = False
    for i in estoque:
        if i['nome'] == produto['nome']:
            item = True
            i['quant'] = produto['quant']
            if produto['preço'] != 0:
                i['preço'] = produto['preço']
            if produto['val'] != 0:
                i['val'] = produto['val']
            if produto['cat'] != '0':
                i['cat'] = produto['cat']
    if not item:
        estoque.append(produto)
    return


def remove_estoque(produto):
    """Função para retirar um produto do estoque
    Subtrai a quantidade caso essa seja maior que a atual e retorna um erro
    caso tente retirar mais do que a quantidade atual"""

    global estoque
    existe = False
    for i in estoque:
        if i['nome'] == produto['nome']:
            existe = True
            if i['quant'] >= produto['quant']:
                i['quant'] -= produto['quant']
                print('SUCCESS')
            else:
                print('ERROR')
    if not existe:
        print('ERROR')


def produto_caixa(dado):
    """Define um dicionário que atuará como produto para a venda no caixa
    As suas caracteríscias consistem no nome, quantidade e valor da compra"""

    produto = {'nome': dado[0], 'quant': int(dado[1]), 'valor': 0}
    return produto


def venda(produto):
    """Função para realizar a venda de um produto
    Subtrai a quantidade vendida do estoque e atualiza a chave 'valor' do produto
    com o preço a ser adicionado no caixa"""

    global estoque
    for i in estoque:
        if i['nome'] == produto['nome']:
            i['quant'] = i['quant'] - produto['quant']
            produto['valor'] = produto['quant'] * i['preço']


def leitura_data(dado):
    """Formata a data recebida no formado DDMMAAAA para uma lista [ano, mes, dia]"""

    dia = dado // 1000000
    dado -= dia * 1000000
    mes = dado // 10000
    ano = dado - (mes * 10000)
    return [ano, mes, dia]


def conta_dias(dado):
    """Baseado na biblioteca datetime, utiliza da classe timedelta para definir
    a diferença de dias entre duas datas, a validade do produto e o dia da operação"""

    global data
    dado = int(dado)
    dado = leitura_data(dado)
    data1 = date(dado[0], dado[1], dado[2])
    return (data1 - data).days


ask = 1                                                 # estoque, caixa ou relatório
estoque = []                                            # cria estoque do zero
caixa = 0                                               # caixa começa zerado

while ask != 0:
    ask = int(input())
    if ask == 1:                                        # operando como estoque
        quant = int(input())                            # quantidade a ser computada
        for i in range(quant):
            dado = input().split()
            produto = entrada_de_dado(dado)
            if dado[0] == '0':
                adiciona_estoque(produto)
            elif dado[0] == '1':
                remove_estoque(produto)
    elif ask == 2:                                         # modo caixa
        quant = int(input())                               # quantidade a ser comprada
        for i in range(quant):
            dado = input().split()
            produto = produto_caixa(dado)
            venda(produto)
            caixa += produto['valor']

data = leitura_data(int(input()))                           # formatação da data
data = date(data[0], data[1], data[2])

print('* ESTOQUE')
categorias = []
for i in estoque:
    if i['quant'] != 0:
        categorias.append(i['cat'])
categorias = set(categorias)
categorias = sorted(categorias)
categorias = list(categorias)                               # lista de categorias em ordem
for i in categorias:
    print(f'- {i}')
    lista = []
    for j in estoque:
        if j['cat'] == i and j['quant'] != 0:
            print(j['nome'] + ' ' + str(j['quant']))
print(f'* SALDO {caixa:.2f}')

reposicao = []
for i in estoque:
    if i['quant'] == 0:
        reposicao.append(i['nome'])
reposicao = sorted(reposicao)
if reposicao:
    print('* REPOSICAO')
    for item in reposicao:
        print(item)

promocao = []
for i in estoque:
    if conta_dias(i['val']) <= 7 and i['quant'] != 0:
        promocao.append(i['nome'])
promocao = sorted(promocao)
if promocao:
    print('* PROMOCAO')
    for item in promocao:
        print(item)
