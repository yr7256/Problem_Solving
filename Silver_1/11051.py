from math import factorial
N, K = map(int, input().split())
result = factorial(N)//(factorial(N-K)*factorial(K))
print(result % 10007)
