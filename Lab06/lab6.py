
class Salas:
    """Classe utilizada para manipulaçõa e armazenamento das salas utilizadas no mapa do jogo"""

    def __init__(self, num=0, item='', porta1=0, porta2=0,
                 porta3=0, porta4=0, clone=False):
        self._item = item
        self.num = num
        self.porta1 = porta1
        self.porta2 = porta2
        self.porta3 = porta3
        self.porta4 = porta4
        self._clone = clone

    def __str__(self):
        """Método para definir como a classe vai ser printada (seguindo modelo conforme o lab.)"""

        if self.item == "":
            return f"Você está na sala de número {str(self.num)} e dela você pode ir para as salas [{str(self.porta1)}, {str(self.porta2)}, {str(self.porta3)}, {str(self.porta4)}]"
        else:
            return f"Você está na sala de número {str(self.num)} ela contém um baú com {str(self._item)} e dela você pode ir para as salas [{str(self.porta1)}, {str(self.porta2)}, {str(self.porta3)}, {str(self.porta4)}]"

    def __repr__(self):
        """Método para representação da lista não necessariamente com o print (usado ao longo do desenvolvimento do código)"""

        if self.item in '':
            return "Sala " + str(self.num)
        else:
            return"Sala " + str(self.num) + " com " + str(self._item)

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, item):
        self._item = item

    @property
    def clone(self):
        return self._clone

    @clone.setter
    def clone(self, clone):
        print(f"DEBUG - O clone está na sala: {self.num}")
        self._clone = clone

    def set_portas(self):
        """Método para configuração do número da sala e das suas portas (salas adjacentes) a partir de uma lista
        no formato [número da sala; porta1; porta2; porta3; porta4]"""

        n = input().split()
        self.num = n[0]
        self.porta1 = n[1]
        self.porta2 = n[2]
        self.porta3 = n[3]
        self.porta4 = n[4]


class Bot:
    """Classe para utilização do bot, controlar a sua sala atual e o seu inventário"""

    def __init__(self, bolsa=0, invent=None, local=0):
        if invent is None:
            invent = []
        self._bolsa = bolsa
        self.invent = invent
        self.local = local

    @property                                                                   # a bolsa representa o tamanho do inventário do bot
    def bolsa(self):
        return self._bolsa

    @bolsa.getter
    def bolsa(self):
        return self._bolsa

    def tam_bolsa(self):
        """Define o tamanho do inventário do bot"""

        self._bolsa = int(input())

    def get_item(self):
        """Função para pegar o item de uma sala
        Automaticamente zera o item dessa sala e não realiza a ação caso o inventário estiver cheio"""

        global sala_atual                                                       # indicador de sala utilizado ao longo do programa
        if sala_atual.item != '' and len(self.invent) < self.bolsa:             # checa se existe espaço no inventário e item na sala
            aux = sala_atual.item
            sala_atual.item = ''                                                # zera o item da sala
            self.invent.append(aux)
            print(f'{aux} adicionado ao inventário')
        elif len(self.invent) == self.bolsa:
            print("Inventário cheio!")


# PROGRAMA PRINCIPAL
print('''Bem-vindo as Aventuras de Sarah 2.0
Sarah acorda no saguão do antigo castelo de sua família,ela tem a oportunidade única de derrotar o seu clone maligno que se apoderou do reino.
Para isso ela deve encontrar o baú da sua família que contém a espada mágica que apenas a verdadeira herdeira pode utilizar.
Na sala onde está Sarah vê várias portas. Qual é a sua próxima ação?''')

mapa = []                           # trabalhando com o mapa como uma lista de salas
bot = Bot()                         # criação do objeto 'bot' desconfigurado

n_salas = int(input())              # input do número de salas
for i in range(n_salas):
    x = Salas()                     # laço que, junto da função set_portas,
    Salas.set_portas(x)             # configura todas as salas do mapa
    mapa.append(x)

n_itens = int(input())              # input do número de itens
for i in range(n_itens):            # "0 item"
    y = input().split()             # --> "0", "espada"   [0]   [1]
    id_sala = int(y[0])             # ponteiro para a sala que receberá o item
    mapa[id_sala].item = y[1]       # item a ser adicionado

n_clone = int(input())
mapa[n_clone].clone = True          # setta a característica do clone verdade em uma das salas

n_bot = int(input())
bot.local = n_bot                   # define no bot sua sala de início
Bot.tam_bolsa(bot)                  # define o tamanho do inventário do bot

ordem = input().split()             # lista com as salas que serão percorridas
seq = []
for i in ordem:                     # laço para transformar os itens da lista em ints
    seq.append(int(i))

cont = -1                           # contador como ponteiro para indicar qual sala será a próxima
fim = False                         # auxiliar para indicar que o bot pegou uma poção

for f in range(len(seq)+1):         # laço para a movimentação do bot
    x = bot.local
    sala_atual = mapa[x]            # chama a sala em que o bot se encontra
    encontro = sala_atual.clone
    if encontro:                    # testa para ver se o bot e o clone não se encontraram
        break                       # lembrando que a característica Sala.clone é booleana
    print(sala_atual)
    item_ = sala_atual.item
    if sala_atual.item != '':
        print(f'Pegar {item_}')
        Bot.get_item(bot)
        if item_ == 'poção':
            fim = True
            break
    cont += 1
    bot.local = seq[cont]           # move o bot para a próxima sala
    print(f'Mover para sala {bot.local}')

if fim:                             # fim com a poção
    print('Você pegou a poção da morte e virou pó instantaneamente. Tente novamente...')
else:
    if 'espada' in bot.invent:      # fim com o encontro e o bot tem a espada
        print('Você derrotou o clone maligno com a espada mágica! Com a Sarah no reino o mundo pode voltar ao equilíbrio.')
        print('PARABÉNS!')
    else:                           # fim com o encontro e bot sem espada
        print('Infelizmente você encontrou o clone sem a espada das fadas e foi derrotado. Tente novamente...')
