# n = int(input())
# dp = [1, 1]
# for i in range(2, n+1):
#     dp.append((dp[i-1]+dp[i-2]) % 10)
# print(dp[n])

def fib(i):
    if not A.get(i):
        if i % 2 == 1:
            A[i] = (fib((i+1)//2)**2+fib((i-1)//2)**2) % num
        else:
            A[i] = (fib(i+1)-fib(i-1)) % num
    return A[i]


A = {0: 0, 1: 1, 2: 1}
num = 10
n = int(input())
print(fib(n+1))
