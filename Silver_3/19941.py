N, K = map(int, input().split())
lst = list(input())
count = 0
for i in range(N):
    if lst[i] == 'P':
        for j in range(max(i-K, 0), min(N, i+K+1)):
            if lst[j] == 'H':
                lst[j] = 'O'
                count += 1
                break
print(count)
