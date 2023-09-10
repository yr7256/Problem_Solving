T = int(input())
for _ in range(T):
    d = []
    x, y = input().split()
    for i in range(len(x)):
        d.append((ord(y[i])-ord(x[i]))%26)
    print('Distances:', *d)