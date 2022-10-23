'''
a**2+b**2=c**2
이렇게 하면 시간초과 걸릴거 같으니까
sum(list)=2*max(list) 이런느낌으로
'''
# 메모리 초과
# from itertools import combinations

# N = int(input())
# lst = [list(map(int, input().split())) for _ in range(N)]
# combi = list(combinations(lst, 3))
# count = 0
# for points in combi:
#     p_list = []
#     for i in range(2):
#         for j in range(i+1, 3):
#             p_list.append((points[i][1]-points[j][1]) **
#                           2+(points[i][0]-points[j][0])**2)
#     if sum(p_list) == 2*max(p_list):
#         count += 1
# print(count)

import sys
input = sys.stdin.readline
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
count = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            p1, p2, p3 = lst[i], lst[j], lst[k]
            a = (p1[0]-p2[0])**2+(p1[1]-p2[1])**2
            b = (p2[0]-p3[0])**2+(p2[1]-p3[1])**2
            c = (p3[0]-p1[0])**2+(p3[1]-p1[1])**2
            if a+b+c == max(a, b, c)*2:
                count += 1
print(count)
# 이 문제 악랄하다...시간초과를 내는 방법이 너무 많다...