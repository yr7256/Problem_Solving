from collections import deque
nums = [False, False]+[True]*(9999)
plist = []
for i in range(2, 10000):
    if nums[i]:
        plist.append(i)
        for j in range(2*i, 10000, i):
            nums[j] = False


def bfs():
    queue = deque()
    queue.append([start, 0])
    visited = [0]*10000
    visited[start] = 1
    while queue:
        now, count = queue.popleft()
        now_list = str(now)
        if now == end:
            return count
        for i in range(4):
            for j in range(10):
                isprime = int(now_list[:i]+str(j)+now_list[i+1:])
                if visited[isprime] == 0 and nums[isprime] and isprime >= 1000:
                    visited[isprime] = 1
                    queue.append([isprime, count+1])


T = int(input())
for i in range(T):
    start, end = map(int, input().split())
    result = bfs()
    if result == None:
        print('Impossible')
    else:
        print(result)
