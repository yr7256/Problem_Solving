def fib(i):
    if not A.get(i):
        if i % 2 == 1:
            A[i] = (fib((i+1)//2)**2+fib(((i+1)//2)-1)**2) % num
        else:
            A[i] = fib(i+1)-fib(i-1)
    return A[i]


A = {0: 0, 1: 1, 2: 1}
n = int(input())
num = 1000000007
print(fib(n) % num)
