'''
일반적인 배낭 문제!
체력보다 떨어지는 기쁨이 크면 갱신x
작으면 갱신 시켜보자!
포인트는 이것!
허용 용량보다 무게가 크면
d[i][j] = d[i-1][j]
허용 용량보다 작으면 갱신
d[i][j] = max(d[i-1][j], d[i-1][j-weight]+value)
'''
N = int(input())
L = [0]+list(map(int, input().split()))
J = [0]+list(map(int, input().split()))
d = [[0]*101 for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, 101):
        if L[i] > j:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-L[i]]+J[i])
print(d[N][99])