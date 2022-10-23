from collections import deque
import sys
input = sys.stdin.readline
for i in range(int(input())):
    S = input().strip()
    left = deque([])
    right = deque([])
    for i in S:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)
    print(''.join(left+deque(reversed(right))))
