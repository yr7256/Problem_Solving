M = int(input())
N = int(input())
p_n = []
for i in range(M, N+1):
    for j in range(2, i+1):
        if i % j == 0:
            if i == j:
                p_n.append(i)
            break
if len(p_n) == 0:
    print(-1)
else:
    print(sum(p_n))
    print(p_n[0])
