N = int(input())
K = int(input())
lst = [0]*(N+1)
for i in range(2, N+1):
    if lst[i] == 0:
        for j in range(i, N+1, i):
            if j % i == 0:
                lst[j] = max(lst[j], i)
ans = 0
for i in range(1, N+1):
    if lst[i] <= K:
        ans += 1
print(ans)