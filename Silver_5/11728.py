N, M = map(int, input().split())
S = []
S.extend(list(map(int, input().split())))
S.extend(list(map(int, input().split())))
S.sort()
print(*S)
