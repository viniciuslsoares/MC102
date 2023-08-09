q = int(input())
T = float(input())
C = float(input())
n = int(input())
tot = 0
for i in range(1, q+1):
    Vi = (T * i) + (T * C)
    tot += Vi
    print(f'{i} {Vi:.2f} {tot:.2f}')
print(f'{tot:.2f}')
x = 1
a = n
while n <= tot:
    print(n)
    x = x + 1
    n = a * x
print(x - 1)
print('BATERIA DE TESTES TERMINADA')
