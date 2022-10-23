T = int(input())
for i in range(T):
    S = list(input().split())
    for j in S:
        print(j[::-1], end=' ')
