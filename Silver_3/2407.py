from math import factorial
N, M = map(int, input().split())
print(factorial(N)//(factorial(N-M)*factorial(M)))
