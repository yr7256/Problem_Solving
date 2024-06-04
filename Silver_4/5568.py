from itertools import permutations
import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
cards = [input().strip() for _ in range(n)]
print(set(''.join(i) for i in permutations(cards,k)))
