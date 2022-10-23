T = int(input())
for i in range(T):
    n = int(input())
    s = []
    for j in range(2):
        s.append(list(map(int, input().split())))
    for k in range(1, n):
        if k == 1:
            s[0][k] += s[1][k-1]
            s[1][k] += s[0][k-1]
        else:
            s[0][k] += max(s[1][k-1], s[1][k-2])
            s[1][k] += max(s[0][k-1], s[0][k-2])
    print(max(s[0][-1], s[1][-1]))