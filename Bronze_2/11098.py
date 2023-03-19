n = int(input())
for _ in range(n):
    p = int(input())
    a, b = 0, ''
    for _ in range(p):
        cost, name = input().split()
        if a < int(cost):
            a = int(cost)
            b = name
    print(b)