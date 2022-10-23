N, M = map(int, input().split())
egg = [int(input()) for i in range(M)]
price = 0
pro = 0
egg.sort(reverse=True)
for i in range(M):
    if i+1 >= N:
        p = egg[i]*N
    else:
        p = egg[i]*(i+1)
    if pro < p:
        price = egg[i]
        pro = p
print(price, pro)
