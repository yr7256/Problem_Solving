import sys
from itertools import combinations
input = sys.stdin.readline
N, M = map(int, input().split())
maps = [list(map(int, input().split())) for i in range(N)]
house = []
store = []
for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            house.append((i, j))
        elif maps[i][j] == 2:
            store.append((i, j))
picked_store = list(combinations(store, M))
result = []
for i in range(len(picked_store)):
    store_distance = 0
    for j in house:
        distance_list = []
        for k in picked_store[i]:
            distance = abs(k[0]-j[0])+abs(k[1]-j[1])
            distance_list.append(distance)
        store_distance += min(distance_list)
    result.append(store_distance)
print(min(result))
# for picked_store in list(combinations(store, M)):
#     store_distance = 0
#     for j in house:
#         distance_list = []
#         for x, y in picked_store:
#             distance = abs(x-j[0])+abs(y-j[1])
#             distance_list.append(distance)
#         store_distance += min(distance_list)
#     result.append(store_distance)
# print(result)
