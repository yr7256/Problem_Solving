from collections import Counter
import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    n = int(input())
    item = []
    for _ in range(n):
        a, b = input().split()
        item.append(b)
    # print(item)
    item_c = Counter(item)
    count = 1
    for i in item_c:
        count *= item_c[i]+1
    print(item_c)
    print(count-1)
