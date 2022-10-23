# N = int(input())
# dic = {}
# for i in range(N):
#     num = int(input())
#     if num in dic:
#         dic[num] += 1
#     else:
#         dic[num] = 1
# dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
# print(dic[0][0])

from collections import Counter
import sys
input = sys.stdin.readline
N = int(input())
cards = [int(input()) for _ in range(N)]
count = Counter(sorted(cards))
print(count.most_common(1)[0][0])
