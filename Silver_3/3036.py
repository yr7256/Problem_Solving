from math import gcd
N = int(input())
ring = list(map(int, input().split()))
for i in range(1, N):
    print(ring[0]//gcd(ring[0], ring[i]),
          ring[i]//gcd(ring[0], ring[i]), sep='/')
