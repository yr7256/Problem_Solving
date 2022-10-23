import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
a_count = 0
b_count = 0
win_list = []
for i in range(N):
    if A[i] == 1:
        if B[i] == 2:
            b_count += 1
            # if a_count != 0:
            win_list.append(a_count)
            win_list.append(b_count)
            a_count = 0
        elif B[i] == 3:
            a_count += 1
            # if b_count != 0:
            win_list.append(a_count)
            win_list.append(b_count)
            b_count = 0
    elif A[i] == 2:
        if B[i] == 1:
            a_count += 1
            # if b_count != 0:
            win_list.append(a_count)
            win_list.append(b_count)
            b_count = 0
        elif B[i] == 3:
            b_count += 1
            # if a_count != 0:
            win_list.append(a_count)
            win_list.append(b_count)
            a_count = 0
    elif A[i] == 3:
        if B[i] == 1:
            b_count += 1
            # if a_count != 0:
            win_list.append(a_count)
            win_list.append(b_count)
            a_count = 0
        elif B[i] == 2:
            a_count += 1
            # if b_count != 0:
            win_list.append(a_count)
            win_list.append(b_count)
            b_count = 0
    if A[i] == B[i]:
        if a_count > b_count:
            b_count = 1
            win_list.append(a_count)
            a_count = 0
        elif b_count > a_count:
            a_count = 1
            win_list.append(b_count)
            b_count = 0
print(win_list)
