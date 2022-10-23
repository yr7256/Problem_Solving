from collections import deque
N = int(input())
A = []
for i in range(1, N+1):
    A.append(i)
A = deque(A)
while len(A) > 1:
    A.popleft()
    A.append(A.popleft())
print(A.pop())
