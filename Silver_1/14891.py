from collections import deque
import sys
input = sys.stdin.readline
gear = [deque(list(map(int, input().rstrip()))) for i in range(4)]
K = int(input())
method = deque()
for i in range(K):
    method.append(list(map(int, input().split())))
while method:
    num, direction = method.popleft()
    num -= 1
    temp_right = gear[num][2]
    temp_left = gear[num][6]
    temp_direction = direction
    gear[num].rotate(direction)
    direction = temp_direction
    for i in range(num-1, -1, -1):
        if gear[i][2] != temp_left:
            temp_left = gear[i][6]
            direction *= -1
            gear[i].rotate(direction)
        else:
            break
    direction = temp_direction
    for i in range(num+1, 4):
        if gear[i][6] != temp_right:
            temp_right = gear[i][2]
            direction *= -1
            gear[i].rotate(direction)
        else:
            break
answer = 0
for i in range(4):
    if gear[i][0] == 1:
        answer += 2**i
print(answer)
