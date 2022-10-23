from collections import deque
N, K = map(int, input().split())
people = deque([])
answer = []
for i in range(1, N+1):
    people.append(i)
while len(people) != 0:
    for i in range(K):
        people.append(people.popleft())
    answer.append(people.pop())
print('<'+', '.join(map(str, answer))+'>')
