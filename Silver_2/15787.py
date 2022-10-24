import sys
input = sys.stdin.readline
N, M = map(int, input().split())
trains = [0]*N
for _ in range(M):
    command = list(map(int, input().split()))
    i = command[1]-1
    if len(command) == 3:
        x = command[2]-1
        if command[0] == 1:
            trains[i] |= 1 << x
        else:
            trains[i] &= ~(1 << x)
    else:
        if command[0] == 3:
            trains[i] <<= 1
            trains[i] &= ~(1 << 20)
        else:
            trains[i] >>= 1
print(len(set(trains)))
# N, M = map(int, input().split())
# trains = [0]*N
# for _ in range(M):
#     command = list(map(int, input().split()))
#     i = command[1]-1
#     if len(command) == 3:
#         x = command[2]-1
#         if command[0] == 1:
#             trains[i] |= 1 << x
#         else:
#             trains[i] &= ~(1 << x)
#     else:
#         if command[0] == 3:
#             trains[i] <<= 1
#             trains[i] &= ~(1 << 20)
#         else:
#             trains[i] >>= 1
# print(len(set(trains)))