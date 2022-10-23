import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    N, M = map(int, input().split())
    Queue = deque(list(map(int, input().split())))
    index = deque(list(range(N)))
    count = 0
    while Queue:
        if max(Queue) == Queue[0]:
            count += 1
            Queue.popleft()
            if index.popleft() == M:
                print(count)
                break
        else:
            Queue.append(Queue.popleft())
            index.append(index.popleft())
