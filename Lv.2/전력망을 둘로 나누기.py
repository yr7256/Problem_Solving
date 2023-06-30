from collections import deque


def bfs(arr, start, n):
    visited = [0]*(n+1)
    queue = deque([start])
    visited[start] = 1
    count = 0
    while queue:
        current = queue.popleft()
        count += 1
        for next in arr[current]:
            if not visited[next]:
                visited[next] = 1
                queue.append(next)
    return count


def solution(n, wires):
    answer = 100
    for i in range(n-1):
        ori_wire = wires[i]
        wires[i] = [0, 0]
        route = [[] for _ in range(n+1)]
        for wire in wires:
            route[wire[0]].append(wire[1])
            route[wire[1]].append(wire[0])
        for j in range(1, n+1):
            answer = min(answer, abs(bfs(route, j, n)*2-n))
        wires[i] = ori_wire
    return answer