T = int(input())
for i in range(T):
    N = int(input())
    s = []
    for i in range(N):
        a, b = input().split()
        s.append((a, int(b)))
    s.sort(key=lambda x: -x[1])
    print(s[0][0])
