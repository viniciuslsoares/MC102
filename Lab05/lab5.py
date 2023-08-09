cont = 0        # contador para random() saber se usa seed/resultado anterior
x1 = 0          # registrador para o resultado x(n-1) de random()


def random():
    global seed, cont, x1
    if cont == 0:
        cont += 1
        x1 = ((7 * seed) + 111) % 1024
    else:
        xn = ((7 * x1) + 111) % 1024
        x1 = xn
    print(f'MENSAGEM DEBUG - número gerado: {x1}')
    return x1


def soco(ataque, defesa):
    m = random() % 3    # [0, 2]
    if (ataque - defesa) < 0:
        return 0
    else:
        return m * (ataque - defesa)


def arremesso_de_facas(ataque):
    n = random() % 6    # [0, 5]
    dano = 0
    for i in range(1, n+1):
        dano += ataque // (3 ** i)
    return dano


def invocacao_de_fadas():
    global status
    p = random() % 100      # [0, 99]
    q = random()            # [0, 1023]
    if q < 100 and q % 2 != 0:
        return p, q, 1      # 1 indica que adiciona ao ataque
    elif q % 2 == 0 and q < 100 and q != 0:
        return p, q, 2      # 2 indica que adiciona à defesa
    elif q >= 1019:
        q = 0
        return p, q, 3      # 3 indica monstro
    else:
        return p, q, 4      # 4 indica que não adiciona ataque nem defesa


def teste_morto():
    global status, ind
    if vidaS <= 0:
        status = 1            # 1 indica que Sarha morreu
    elif vidaC <= 0:
        status = 2            # 2 indica que o Clone morreu
    elif ind == 3:
        status = 3            # 3 indica monstro
    else:
        status = 0            # 0 indica que nenhum dos dois morreu


def dano(nome, valor):
    print(f'{nome} sofreu {valor} pontos de dano!')


sarah = input().split()     # Atributos Sarah
vidaS = int(sarah[0])
ataS = int(sarah[1])
defS = int(sarah[2])
clone = input().split()     # Atributos Clone
vidaC = int(clone[0])
ataC = int(clone[1])
defC = int(clone[2])
seed = int(input())         # Entrada da seed para random()
status = 0                  # Indica o fim do combate
turno = 0                   # Se turno ímpar, Sarah joga/ turno par, Clone joga
ind = 0                     # Indica se monstro

while status == 0:
    turno += 1
    move = input()
    if move == 'soco':
        if turno % 2 != 0:
            valor = soco(ataS, defC)
            dano('O clone', valor)
            vidaC = vidaC - valor
        elif turno % 2 == 0:
            valor = soco(ataC, defS)
            dano('Sarah', valor)
            vidaS = vidaS - valor
    elif move == 'facas':
        if turno % 2 != 0:
            valor = arremesso_de_facas(ataS)
            dano('O clone', valor)
            vidaC = vidaC - valor
        elif turno % 2 == 0:
            valor = arremesso_de_facas(ataC)
            dano('Sarah', valor)
            vidaS = vidaS - valor
    elif move == 'fada':
        if turno % 2 != 0:
            lvalor = invocacao_de_fadas()
            ind = lvalor[2]
            vidaS += lvalor[0]
            print(f'Sarah ganhou {lvalor[0]} pontos de vida!')
            if ind == 1:
                ataS += lvalor[1]
                print(f'Sarah ganhou {lvalor[1]} pontos de ataque!')
            elif ind == 2:
                defS += lvalor[1]
                print(f'Sarah ganhou {lvalor[1]} pontos de defesa!')
        elif turno % 2 == 0:
            lvalor = invocacao_de_fadas()
            vidaC += lvalor[0]
            ind = lvalor[2]
            print(f'O clone ganhou {lvalor[0]} pontos de vida!')
            if ind == 1:
                ataC += lvalor[1]
                print(f'O clone ganhou {lvalor[1]} pontos de ataque!')
            elif ind == 2:
                defC += lvalor[1]
                print(f'O clone ganhou {lvalor[1]} pontos de defesa!')
    teste_morto()

if status == 1:
    print('Sarah foi derrotada...')
elif status == 2:
    print('''O clone foi derrotado! Sarah venceu!
FIM - PARABENS''')
elif status == 3:
    if turno % 2 != 0:
        print('''O quê? A fada trouxe um monstro gigante com ela!
O Clone e o castelo foram destruídos,
e Sarah agora tem um novo pet.
FINAL SECRETO - PARABENS???''')
    elif turno % 2 == 0:
        print('''O quê? A fada trouxe um monstro gigante com ela!
Sarah foi derrotada...''')
