
dia = int(input())
semana = str(input())
preço = float(input())
if dia % 7 == 0:
    preço = preço*0.5
elif semana == 'sexta-feira':
    preço = preço*0.75
else:
    preço = preço - dia
if preço < 0:
    preço = 0
print(f'{preço:.2f}')
if semana == 'segunda-feira':
    print('É um dia terrível, você não devia ter saído da cama.')
elif semana == 'sábado' or semana == 'domingo':
    print('Agradecemos a preferência, tenha um ótimo fim de semana!')
else:
    print(f'Agradecemos a preferência, tenha uma ótima {semana}!')
