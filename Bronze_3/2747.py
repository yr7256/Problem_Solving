def fib(i):
    if not A.get(i):
        if i % 2 == 1:
            A[i] = fib((i+1)//2)**2+fib((i-1)//2)**2
        else:
            A[i] = fib(i+1)-fib(i-1)
    return A[i]


A = {0: 0, 1: 1, 2: 1}
n = int(input())
print(fib(n))
