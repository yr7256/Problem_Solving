import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
queue = deque()
for _ in range(N):
    s = list(map(int, input().split()))
    if s[0] == 1:
        queue.appendleft(s[1])
    if s[0] == 2:
        queue.append(s[1])
    if s[0] == 3:
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    if s[0] == 4:
        if queue:
            print(queue.pop())
        else:
            print(-1)
    if s[0] == 5:
        print(len(queue))
    if s[0] == 6:
        print(0 if queue else 1)
    if s[0] == 7:
        print(queue[0] if queue else -1)
    if s[0] == 8:
        print(queue[-1] if queue else -1)