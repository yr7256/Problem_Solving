N = int(input())
N_list = set(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))
for i in check:
    if i in N_list:
        print(1, end=' ')
    else:
        print(0, end=' ')
# N = int(input())
# N_list = list(map(int, input().split()))
# M = int(input())
# check = list(map(int, input().split()))
# N_list.sort()


# def search(num):
#     start = 0
#     end = N-1
#     while start <= end:
#         mid = (start+end)//2
#         if N_list[mid] == num:
#             return 1
#         elif N_list[mid] < num:
#             start = mid+1
#         else:
#             end = mid-1
#     return 0


# for i in check:
#     print(search(i), end=' ')
