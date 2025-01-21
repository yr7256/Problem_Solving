'''
bisect 내장함수
from bisect import bisect_left
x = bisect_left(arr, num) 형식으로 사용할 수 있다.
'''
from collections import deque


def bisect(n):
    s, e = 0, len(arr)
    while s < e:
        m = (s+e)//2
        if arr[m] < n:
            s = m+1
        else:
            e = m
    return e


N = int(input())
A = list(map(int, input().split()))
arr = [-1e9-1]
arr_idx = []
for num in A:
    if arr[-1] < num:
        arr.append(num)
    else:
        arr[bisect(num)] = num
    arr_idx.append(bisect(num))
temp = len(arr[1:])
queue = deque()
for i in range(len(arr_idx)-1, -1, -1):
    if arr_idx[i] == temp:
        temp -= 1
        queue.appendleft(A[i])
print(len(queue))
print(*queue)
