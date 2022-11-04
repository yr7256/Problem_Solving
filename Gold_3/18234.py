N, T = map(int, input().split())
ans = 0
nutrition = []
for i in range(N):
    w, p = map(int, input().split()) # 당근, 영양제
    ans += w
    nutrition.append(p)
nutrition.sort()
for i in range(T-N, T):
    ans += nutrition[i-(T-N)]*i
print(ans)
'''
5일까지 보면
1 2 3
4 11 10
7 20 17
10 29 24
13 38 31
맨 마지막 날부터 계산해보기 3 4 5 일 먹으면 되잖아
p
sort.()
for i in range(T-N, T):
    ans +=
'''
