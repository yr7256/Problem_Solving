def catch(j):
    global ans
    for i in range(R):
        if arr[i][j]:
            ans += arr[i][j][0][0]
            arr[i][j] = []
            break


# 상어 이동
def move():
    global arr
    temp = [[[] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j]:
                x, y = i, j
                size, speed, direction = arr[i][j][0]
                cnt = 0
                if speed:
                    while cnt < speed:
                        x1 = x + dx[direction]
                        y1 = y + dy[direction]
                        if x1 < 0 or x1 >= R or y1 < 0 or y1 >= C:
                            direction = dic[direction]
                            continue
                        else:
                            cnt += 1
                            x, y = x1, y1
                else:
                    x1, y1 = x, y
                temp[x1][y1].append([size, speed, direction])
                if len(temp[x1][y1]) > 1:
                    temp[x1][y1].sort(reverse=True)
                    temp[x1][y1] = [temp[x1][y1][0]]
    arr = temp


dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]
R, C, M = map(int, input().split())
arr = [[[] for _ in range(C)] for _ in range(R)]
for i in range(M):
    r, c, s, d, z = map(int, input().split())  # 위치, 속력, 이동 방향, 크기
    arr[r-1][c-1].append([z, s, d])
dic = {1: 2, 2: 1, 3: 4, 4: 3}
ans = 0
for i in range(C):
    catch(i)
    move()
print(ans)
'''
사람 이동 -> 상어 잡기 -> 상어 이동
같은 자리 상어가 더 작으면 먹힌다 -> 1개 이상이면 sort해서 젤 큰거 남기고 삭제
없애는 건 그냥 arr[i][j] = [] 느낌으로 접근해보자.
speed 0 일때는 어떻게 할건데? -> x1, y1 = x, y 그대로 놔두자
'''
