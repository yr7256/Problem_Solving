T = int(input())
for _ in range(T):
    a, b = 0, 100
    for i in map(int, input().split()):
        if not i % 2:
            a += i
            if i < b:
                b = i
    print(a, b)