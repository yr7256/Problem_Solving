N = int(input())
print(sum(min(N, i) for i in map(int, input().split())))
