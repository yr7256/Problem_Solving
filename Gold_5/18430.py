'''
백트래킹
중심 기준으로 [0,-1,1,0],[0,-1,-1,0],[0,1,-1,0],[0,1,1,0] 4방향 사용하자
넴모넴모를 생각하자 오른쪽으로 한칸씩 가면서 끝이면 한줄 바꾸기
맨 마지막에서 ans 갱신해주자
'''


def back(i, j, temp):  # 가로, 세로, 합
    global ans
    if j == M:
        i += 1
        j = 0
    if i == N:
        ans = max(ans, temp)
        return
    # 방문 안했을때 들어가야함
    if not visited[i][j]:
        for k in range(4):
            x1, y1, x2, y2 = i+dic[k][0], j+dic[k][1], i+dic[k][2], j+dic[k][3]
            if 0 <= x1 < N and 0 <= y1 < M and 0 <= x2 < N and 0 <= y2 < M and not visited[x1][y1] and not visited[x2][y2]:
                visited[i][j] = visited[x1][y1] = visited[x2][y2] = 1
                back(i, j+1, temp+arr[i][j]*2+arr[x1][y1]+arr[x2][y2])
                visited[i][j] = visited[x1][y1] = visited[x2][y2] = 0
    back(i, j+1, temp)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
ans = 0
dic = {0: [0, -1, 1, 0], 1: [0, -1, -1, 0], 2: [0, 1, -1, 0], 3: [0, 1, 1, 0]}
back(0, 0, 0)
print(ans)
