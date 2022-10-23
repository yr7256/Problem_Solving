'''
분산이든 반시계든 시계든 방향순서 다 다르니까 함수 안에서 그냥 dxdy 선언해주자
시계는 우 하 좌 상 순서
반시계는 우 상 좌 하 순서
분산은 그냥 상 하 좌 우 아무렇게나 상관 x
방향대로 쭉 가다가 부딪히면 방향 바꾸는 방법 쓰고 바람에 밀린다고 했으니까
이전 값 저장해주는 수 하나 놓고 계속 바꿔주기
분산은 어떻게 하지.. (생각해보자)
일단 dxdy 놓고 되면 count += 1 해주고 그만큼 빼준다 여기까진 알겠는데
deepcopy를 써야하는건가... (고민중) -> 역시 temp를 써서 더해주는거였다.. 이걸 생각 못하다니 ㅠㅠ
위 아래 돌아가는게 어려울 줄 알았는데 오히려 저 부분에서 많은 시간을 소요했다.
'''


def spread():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    temp = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                piece = arr[i][j]//5
                count = 0
                for k in range(4):
                    x1 = i+dx[k]
                    y1 = j+dy[k]
                    if 0 <= x1 < R and 0 <= y1 < C and arr[x1][y1] != -1:
                        temp[x1][y1] += piece
                        count += 1
                arr[i][j] -= count*piece
    for i in range(R):
        for j in range(C):
            arr[i][j] += temp[i][j]


def clockwise():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    d = 0
    temp = 0
    x0, y0 = purifier_bottom, 1
    while True:
        x1 = x0+dx[d]
        y1 = y0+dy[d]
        if x0 == purifier_bottom and y0 == 0:
            break
        if 0 <= x1 < R and 0 <= y1 < C:
            arr[x0][y0], temp = temp, arr[x0][y0]
            x0, y0 = x1, y1
        else:
            d += 1
            continue


def counterclockwise():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    d = 0
    temp = 0
    x0, y0 = purifier_top, 1
    while True:
        x1 = x0+dx[d]
        y1 = y0+dy[d]
        if x0 == purifier_top and y0 == 0:
            break
        if 0 <= x1 < R and 0 <= y1 < C:
            arr[x0][y0], temp = temp, arr[x0][y0]
            x0, y0 = x1, y1
        else:
            d += 1
            continue


R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
purifier_top, purifier_bottom = 0, 0
for i in range(R):
    if arr[i][0] == -1:
        purifier_top = i
        purifier_bottom = i+1
        break
for _ in range(T):
    spread()
    clockwise()
    counterclockwise()
ans = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] > 0:
            ans += arr[i][j]
# print(arr)
print(ans)
