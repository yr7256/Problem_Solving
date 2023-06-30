from heapq import heappop, heappush


def solution(board):
    N = len(board)
    costs = [[[987654321]*N for _ in range(N)] for _ in range(4)]
    d_info = {0: [0, 1], 1: [1, 0], 2: [0, -1], 3: [-1, 0]}
    queue = [[0, 0, 0, 0], [0, 0, 1, 0]]
    while queue:
        x, y, d, c = heappop(queue)
        for dd in d_info:
            dx, dy = d_info[dd]
            x1, y1 = x+dx, y+dy
            if 0 <= x1 < N and 0 <= y1 < N and not board[x1][y1]:
                temp = c + (100 if d == dd else 600)
                if temp < costs[dd][x1][y1]:
                    costs[dd][x1][y1] = temp
                    heappush(queue, [x1, y1, dd, temp])
    answer = min(costs[i][N-1][N-1] for i in range(4))
    return answer