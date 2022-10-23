N, M = map(int, input().split())
arr = [input() for _ in range(N)]
for i in arr:
    print(i[::-1])
