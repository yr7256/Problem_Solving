# 2번 풀이
# from collections import Counter
# N, M = map(int, input().split())
# lst = Counter(map(int, input().split()))  # dict 형태로
# left, right = 1, max(lst)
# while left <= right:
#     mid = (left+right)//2
#     sum_cut = 0
#     for i, j in lst.items():
#         if i-mid > 0:
#             sum_cut += (i-mid)*j
#             if sum_cut > M:
#                 break
#     if sum_cut < M:
#         right = mid-1
#     else:
#         left = mid+1
# print(right)

# 1번 풀이
N, M = map(int, input().split())
lst = list(map(int, input().split()))  # 나무의 리스트
left, right = 1, max(lst)
flag = True
while left <= right:  # left가 더 커지면 안되니까
    mid = (left+right)//2  # 이분 탐색
    sum_cut = 0  # 자른 나무 길이를 저장
    for i in lst:
        # 나무들에서 나무들이 mid보다 크다면 자르고
        # 그 자른 값은 sum_cut에 저장.
        # sum_cut이 M 넘으면 break.
        if i-mid > 0:
            sum_cut += i-mid
            if sum_cut > M:
                break
    if sum_cut < M:
        right = mid-1
    elif sum_cut > M:
        left = mid+1
    else:  # 같을 때
        flag = False
        break
    # for문 다 돌았을 때(혹은 break 했을 때),
    # sum_cut이 더 작으면 더 아래 쪽을 잘라야 하니까
    # right는 mid보다 작게, 반대는 left는 mid보다 크게
    # 만약 같다면 flag=False하고 break(더 돌 필요x)
if flag:  # flag==True
    print(right)
else:  # Flag==False
    print(mid)
