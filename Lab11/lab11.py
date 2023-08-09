def recebe_linha(arq):
    return arq.readline().rstrip().split()


def converte_lista(list):
    return ' '.join(map(str, list)) + '\n'


def escreve_linhas(lista):
    for item in lista:
        f.write(converte_lista(item))


def conta_parag():
    global parag
    for linhas in arquivo:
        parag += 1
    return


entrada = int(input())
med_leitores = 0                    # A
mais_leitores = 0                   # B1
tit_leitores = ''                   # B2
mais_leitores_final = 0             # C1
tit_leitores_final = ''             # C2
med_cliques = 0                     # D
maior_tempo = 0                     # E
med_parag = 0                       # F

for i in range(entrada):
    nome = input()
    parag = 0
    with open(nome) as arquivo:
        id = recebe_linha(arquivo)                                  # 1
        titulo = recebe_linha(arquivo)                              # nome do arquivo
        leitores_tot = recebe_linha(arquivo)                        # 2 (qnt de leitores)
        leitores_final = recebe_linha(arquivo)                      # 3 (leitores até o final)
        cliques = recebe_linha(arquivo)                             # 4 (cliques)
        tempo = recebe_linha(arquivo)                               # 5 (tempo)
        conta_parag()
    med_leitores += int(leitores_tot[1])                            # A
    med_cliques += int(cliques[1])                                  # D
    med_parag += parag                                              # F
    titulo.pop(0)
    titulo = ' '.join(map(str, titulo))

    if int(leitores_tot[1]) > mais_leitores:
        mais_leitores = int(leitores_tot[1])                        # B1
        tit_leitores = titulo                                       # B2

    if int(tempo[1]) > maior_tempo:
        maior_tempo = int(tempo[1])                                 # E

    if int(leitores_final[1]) > mais_leitores_final:
        mais_leitores_final = int(leitores_final[1])                # C1
        tit_leitores_final = titulo                                 # C2

    novo_arquivo = f'relatorio_{id[1]}.txt'
    lista = [id, leitores_tot, leitores_final, cliques, tempo]
    f = open(novo_arquivo, 'w')
    escreve_linhas(lista)
    f.close()

novo_arquivo = 'relatorio_final.txt'
f = open(novo_arquivo, 'w')
f.write(str(med_leitores//entrada) + '\n')
f.write(f'"{str(tit_leitores).lstrip()}" {mais_leitores}\n')
f.write(f'"{str(tit_leitores_final).lstrip()}" {mais_leitores_final}\n')
f.write(f'{med_cliques//entrada}\n')
f.write(str(maior_tempo) + '\n')
f.write(f'{med_parag //entrada}')
f.close()
