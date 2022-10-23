N, M = map(int, input().split())
S = set([input() for i in range(N)])
count = 0
for i in range(M):
    a = input()
    if a in S:
        count += 1
print(count)
