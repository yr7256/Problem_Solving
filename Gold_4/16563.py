# 시간초과
from collections import defaultdict
import sys
input = sys.stdin.readline
N = int(input())
for num in map(int, input().split()):
    dic = defaultdict(int)
    for i in range(2, N+1):
        while num:
            if not num % i:
                num //= i
                dic[i] += 1
            else:
                break
    for key, value in dic.items():
        print((str(key)+' ')*value, end='')
    print()
