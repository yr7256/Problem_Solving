from math import ceil
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
result = N
for i in A:
    i -= B
    if i < 0:
        continue
    result += ceil(i/C)
print(result)
