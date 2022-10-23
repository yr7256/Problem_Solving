N = int(input())
a = 0
while True:
    if N % 5 == 0:
        a += (N//5)
        print(a)
        break
    N -= 3
    a += 1
    if 0 < N < 3:
        print(-1)
        break
