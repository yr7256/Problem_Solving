from math import gcd
t = int(input())
for _ in range(t):
    num = list(map(int, input().split()))
    sum = 0
    for i in range(1, len(num)):
        for j in range(i+1, len(num)):
            sum += gcd(num[i], num[j])
    print(sum)
