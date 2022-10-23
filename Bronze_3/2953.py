S = []
for i in range(5):
    a = sum(map(int, input().split()))
    S.append(a)
print(S.index(max(S))+1, max(S))
