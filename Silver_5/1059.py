L = int(input())
S = list(map(int, input().split()))
n = int(input())
S.sort()
if n in S:
    print(0)
else:
    min = 0
    max = 0
    for i in S:
        if i < n:
            min = i
        elif i > n and max == 0:
            max = i
    print((max-n)*(n-min)-1)
