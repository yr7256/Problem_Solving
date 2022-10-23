import sys
from math import gcd
input = sys.stdin.readline
N = int(input())
tree = []
gap = []
for i in range(N):
    a = int(input())
    tree.append(a)
for i in range(N-1):
    gap.append(tree[i+1]-tree[i])
max_gap = max(gap)
for i in range(N-1):
    max_gap = gcd(max_gap, gap[i])
answer = (tree[-1]-tree[0])//max_gap-(N-1)
print(answer)
