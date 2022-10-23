from math import gcd
N = int(input())
N_lst = list(map(int, input().split()))
M = int(input())
M_lst = list(map(int, input().split()))
A = 1
B = 1
for i in N_lst:
    A *= i
for i in M_lst:
    B *= i
print('%s' % str(gcd(A, B))[-9:])
