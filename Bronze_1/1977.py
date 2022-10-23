from math import sqrt
M = int(input())
N = int(input())
result = 0
num = 0
for i in range(int(sqrt(N)+1), -1, -1):
    if M <= i**2 <= N:
        result += i**2
        num = i**2
if result == 0:
    print(-1)
else:
    print(result)
    print(num)
