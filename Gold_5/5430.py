import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    p = list(input().rstrip())
    n = int(input())
    nlist = input().rstrip()
    nlist = nlist[1:-1].split(',')
    queue = deque()
    for i in range(n):
        queue.append(nlist[i])
    reverse = False
    error = False
    for i in range(len(p)):
        if p[i] == 'D' and len(queue) == 0:
            error = True
            break
        elif p[i] == 'D' and reverse == False:
            queue.popleft()
        elif p[i] == 'D' and reverse == True:
            queue.pop()
        elif p[i] == 'R':
            if reverse == True:
                reverse = False
            else:
                reverse = True
    sorted_nlist = []
    if error == True:
        print('error')
    else:
        if reverse == False:
            while queue:
                x = queue.popleft()
                sorted_nlist.append(x)
        else:
            while queue:
                x = queue.pop()
                sorted_nlist.append(x)
        print('[' + ','.join(sorted_nlist) + ']')
