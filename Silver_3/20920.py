from collections import defaultdict
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dic = defaultdict(int)
for i in range(N):
    s = input().strip()
    if len(s) >= M:
        dic[s] += 1
dic_list = list(dic.keys())
dic_list.sort(key=lambda x: (-dic[x], -len(x), x))
for i in dic_list:
    print(i)
