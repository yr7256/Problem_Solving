N = list(map(int, input().split()))
S = list(input())
N.sort()
for i in S:
    if i == 'A':
        print(N[0], end=' ')
    elif i == 'B':
        print(N[1], end=' ')
    else:
        print(N[2], end=' ')
