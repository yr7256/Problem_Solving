N, K = map(int, input().split())
num = [0]*(N+1)
count = 0
for i in range(2, N+1):
    for j in range(i, N+1, i):
        if num[j] == 0:
            num[j] = 1
            count += 1
            if count == K:
                print(j)
                break
