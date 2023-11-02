def fib(n):
    x, y = 1, 1
    for i in range(3, n+1):
        x, y = y, x+y
    return y


n = int(input())
print(fib(n), n-2)
