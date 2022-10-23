'''
처음에는 dx dy로 접근했었다. 하지만 도저히 풀리지 않음..
다른 방법을 검색해보니 오른쪽으로 가다가 그 수가 벽에 닿으면 다음 줄 처음으로 가는 방법이 있었다
첫번째 행과 열의 index error를 방지하기 위해서는 벽 하나 만들어줘야 함
어느 칸 찍었을때 왼쪽 위 왼위가 다 0이면 걱정 x. -> arr[x][y] = 1 찍어준다
찍고 재귀 들어갔다가 arr[x][y] = 0 으로 다시 초기화 시켜주기
'''
def dfs(x, y):
    global ans
    if x == N+1:
        ans += 1
        return
    if y == M:
        x1, y1 = x+1, 1
    else:
        x1, y1 = x, y+1
    dfs(x1, y1)
    if not (arr[x-1][y] and arr[x][y-1] and arr[x-1][y-1]):
        arr[x][y] = 1
        dfs(x1, y1)
        # print(arr)
        arr[x][y] = 0


N, M = map(int, input().split())
arr = [[0]*(M+1) for _ in range(N+1)]
ans = 0
dfs(1, 1)
print(ans)
