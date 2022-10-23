'''
student 받아서 defaultdict에 그냥 순서대로 넣자.
한번 더 나오면 그 value만 계속 갱신해주는거고
다 받고나면 value 순으로 정렬하기.
'''
import sys
from collections import defaultdict
input = sys.stdin.readline
K, L = map(int, input().split())
dic = defaultdict(int)
for i in range(L):
    student = input().rstrip()
    dic[student] = i
ans = sorted(dic.keys(), key=lambda x: dic[x])
# for i in range(K):
#     print(ans[i]) <-- 이건 IndexError
count = 0
for i in ans:
    if count == K:
        break
    print(i)
    count += 1      # 이건 왜 되는거야..?