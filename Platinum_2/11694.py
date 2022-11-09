N = int(input())
lst = list(map(int,input().split()))
ans = 0
first = 0
for i in range(N):
    if lst[i] == 1:
        first += 1
    ans ^= lst[i]
if first == N:
    if first % 2:
        ans = 0
    else:
        ans = 1
if ans:
    print('koosaga')
else:
    print('cubelover')
# elif first:
#     if first%2:
#         if ans:
#             print('koosaga')
#         else:
#             print('cubelover')
#     else: # 1이 짝수 자연수개수
#         for i in range(N):
#             if lst[i] != 1:
#                 ans ^= lst[i]
#                 ans ^= 1
#                 break
#         if ans:
#             print('koosaga')
#         else:
#             print('cubelover')
# else:
#     if ans:
#         print('koosaga')
#     else:
#         print('cubelover')
    
