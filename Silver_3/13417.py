from collections import deque
T = int(input())
for _ in range(T):
    N = int(input())
    cards = input().split()
    queue = deque(cards[0])
    target = cards[0]
    for i in range(1, N):
        if target < cards[i]:
            queue.append(cards[i])
        else:
            queue.appendleft(cards[i])
            target = cards[i]
    print(''.join(queue))
