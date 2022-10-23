def fib(i):
    if i == 0:
        return 0
    if not A.get(i):
        if i % 2 == 1:
            A[i] = (fib((i+1)//2)**2+fib((i-1)//2)**2) % num
        else:
            A[i] = (fib(i+1)-fib(i-1)) % num
    return A[i]


A = {0: 0, 1: 1, 2: 1}
num = 10**9
n = int(input())
if n < 0 and not n % 2:
    print(-1)
elif n == 0:
    print(0)
else:
    print(1)
print(fib(abs(n)))
