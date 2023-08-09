op = 0
while op != '0':
    entrada = input()
    valores = entrada.split()
    op = valores[0]
    n1 = int(valores[1])
    n2 = int(valores[2])
    if op == '+':
        print(n1 + n2)
    elif op == '-':
        print(n1 - n2)
    elif op == '*':
        print(n1 * n2)
    elif op == '/':
        print((n1 // n2), (n1 % n2))
    elif op == ';':
        mod = []
        aux = n1 - n2
        if aux < 0:
            aux = aux * -1
        if aux != 0:
            for i in range(1, aux + 1):
                if aux % i == 0:
                    mod.append(i)
            print(*mod)
        else:
            print(0)
