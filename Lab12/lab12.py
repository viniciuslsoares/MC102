from decimal import *
from recipes_decimal import pi
pi = pi()
getcontext().prec = 36


def zeta_func(s):
    """Função zeta necessária para a função de cálculo de distância"""
    soma = 0
    for j in range(1, 101):
        aux = 1 / j ** s
        soma += aux
    return soma


def func(x):
    """Função que calcula a distância para um determinado valor de x"""
    global a, b, c, d
    aux1 = pi + (a * (x.exp())) - zeta_func(((b * x) + pi))
    aux2 = (-1 * ((c * x).sqrt())).exp() + d * ((2 * (pi ** 3)) - x)
    y = Decimal(aux1) / Decimal(aux2)
    return y


def recebe_rota():
    """Função que cria um dicionário representando o planeta com a sua distância e adiciona
    na lista que representa a rota do robo"""
    global rota
    for k in range(entrada):
        planeta = {'nome': input(), 'dist': Decimal(input())}
        rota.append(planeta)


def recebe_param():
    """Função para receber os parâmetros da func de cálculo de distância"""
    global a, b, c, d
    a = Decimal(input())
    b = Decimal(input())
    c = Decimal(input())
    d = Decimal(input())


def busca_bin(dist):
    """Função para realizar a busca binária no intervalo definido"""
    min = Decimal(0)                                            # Início do primeiro intervalo em 0
    max = Decimal(50)                                           # Final do primeiro intervalo em 50
    while True:
        x = (max + min)/2                                       # Valor a ser testado na busca
        y = func(Decimal(x))                                    # Distância referente ao valor testado
        if abs(y - dist) <= dist * Decimal(10 ** -32):          # Verifica se o valor obtido é suficientemente próximo
            break                                               # Considerando a precisão de 10^-32
        elif y > dist:                                          # Se a distância obtida for maior
            max = x                                             # o valor testado passa a ser o novo máximo do intervalo
        elif y < dist:                                          # Se a distância obtida for menor
            min = x                                             # o valor testado passa a ser o novo mínimo do intervalo
    return x                                                    # Retorna o valor de x com precisão de 10^-32


a = b = c = d = 0                                               # define os parâmetros da função a serem modificados
rota = []                                                       # cria a rota zerada
while True:
    entrada = int(input())                                      # recebe a quantidade de planetas na rota
    if entrada == 0: break                                      # quebra o loop se a entrada for 0
    rota = []
    recebe_rota()
    recebe_param()
    mais_dist = 0
    for i in rota:
        if i['dist'] - mais_dist > 0 and \
                func(Decimal(50)) - i['dist'] > 0:              # Encontra o planeta mais longe dentro do limite
            mais_dist = i['dist']                               # máximo de func(50)
            nome = i['nome']                                    # mantém a variável = 0 se todos forem mais longe que
    for item in rota:                                           # func (50) ou armazena o nome do planeta alvo
        if item['nome'] == nome:
            alvo = item['dist']                                 # guarda a distância do planeta alvo
    if mais_dist == 0:
        print('GRAU~~')                                         # printa GRAU~~ caso nenhum planeta seja alcançavel
    else:
        print(nome)                                             # printa o nome do planeta alvo
        tanque = busca_bin(alvo)                                # realiza a busca binária para definir o combustível
        print(f'{tanque:.28f}')                                 # printa o combustível resultado da busca
