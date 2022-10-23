# 첫 번째 방법 (실패) 왔다갔다 하는 케이스에 대응이 안됨.
# N = int(input())
# pillar = [[0, 0]] + [list(map(int, input().split()))
#                      for _ in range(N)]+[[0, 0]]
# pillar.sort()
# ans = 0
# max_index = 0
# max_height = 0
# for i in range(N):
#     if pillar[i][1] > max_height:
#         max_height = pillar[i][1]
#         max_index += 1
# temp = pillar[0][1]
# for i in range(max_index+1):
#     if temp < pillar[i+1][1]:
#         ans += temp*(pillar[i+1][0]-pillar[i][0])
#         temp = pillar[i+1][1]
#     else:
#         ans += temp*(pillar[i+1][0]-pillar[i][0])
# temp = pillar[-1][1]
# for i in range(N-1, max_index-1, -1):
#     if temp < pillar[i-1][1]:
#         ans += temp*(pillar[i][0]-pillar[i-1][0])
#         temp = pillar[i-1][1]
#     else:
#         ans += temp*(pillar[i][0]-pillar[i-1][0])
# print(ans)
"""
max_index 찾은 다음에 그거 기준으로 왼쪽으로, 오른쪽으로 찾기
한꺼번에 곱해서 더하는거보다 그 당시에 가장 큰 수를 계속 answer에 더해준다.
"""
N = int(input())
pillar = [0]*(1001)
max_height = 0
max_index = 0
for _ in range(N):
    L, H = map(int, input().split())
    pillar[L] = H
    if max_height < H:
        max_index = L
        max_height = H
print(pillar)
temp = 0
answer = 0
for i in range(max_index+1):
    temp = max(temp, pillar[i])
    answer += temp
temp = 0
for i in range(1000, max_index, -1):
    temp = max(temp, pillar[i])
    answer += temp
print(answer)
