N, K = map(int, input().split())
count = 0
num = []
for i in range(1, N+1):
    if N % i == 0:
        num.append(i)
if K > len(num):
    print(0)
else:
    print(num[K-1])
