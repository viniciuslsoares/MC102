print('*Que página de meme do Instagram você é?*')
erro = False
pag = ''
print('Qual a sua idade?')
idade = int(input())
print(idade)
if 0 <= idade < 25:
    print('Quantos segundos são necessários para saber se um vídeo é bom?')
    seg = int(input())
    print(seg)
    if 0 < seg <= 5:
        pag = 'Você deveria estar no TikTok'
    elif seg > 5:
        pag = 'Sua página de memes é: @meltmemes'
    else:
        erro = True
elif 25 <= idade <= 40:
    print('Qual banda você gosta mais?')
    banda = input()
    if banda == 'A':
        print('A) Matanza')
        pag = 'Sua página de memes é: @badrockistamemes'
    elif banda == 'B':
        print('B) Iron Maiden')
        pag = 'Sua página de memes é: @badrockistamemes'
    elif banda == 'C' or banda == 'D':
        if banda == 'C':
            print('C) Imagine Dragons')
        else:
            print('D) BlackPink')
        print('São as capivaras os melhores animais da Terra?')
        ask = input()
        if ask == 'Sim':
            print(ask)
            pag = 'Sua página de memes é: @genteboamemes'
        elif ask == 'Não':
            print(ask)
            pag = 'Sua página de memes é: @wrongchoicememes'
        else:
            print('NADA')
            erro = True
elif 40 < idade <= 125:
    print('Que imagem de bom dia você manda no grupo da família?')
    imagem = input()
    if imagem == 'A':
        print('A) Bebê em roupa de flor')
        pag = 'Sua página de memes é: @bomdiabebe'
    elif imagem == 'B':
        print('B) Gato')
        pag = 'Sua página de memes é: @kittykatmsgs'
    elif imagem == 'C':
        print('C) Coração e rosas')
        pag = 'Sua página de memes é: @bomdiaflordodia'
    else:
        print('NADA')
        erro = True
else:
    erro = True
if not erro:
    print('RESULTADO')
    print(pag)
else:
    print('Erro: entrada inválida')
