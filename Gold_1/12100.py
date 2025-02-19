from copy import deepcopy


def move(x, d):
    if d == 0:  # 왼쪽
        for i in range(N):
            target = 0
            for j in range(1, N):
                if x[i][j]:
                    temp = x[i][j]
                    x[i][j] = 0
                    if x[i][target] == 0:
                        x[i][target] = temp
                    elif x[i][target] == temp:
                        x[i][target] *= 2
                        target += 1
                    else:
                        target += 1
                        x[i][target] = temp
    elif d == 1:  # 오른쪽
        for i in range(N):
            target = N-1
            for j in range(N-2, -1, -1):
                if x[i][j]:
                    temp = x[i][j]
                    x[i][j] = 0
                    if x[i][target] == 0:
                        x[i][target] = temp
                    elif x[i][target] == temp:
                        x[i][target] *= 2
                        target -= 1
                    else:
                        target -= 1
                        x[i][target] = temp
    elif d == 2:  # 위쪽
        for j in range(N):
            target = 0
            for i in range(N):
                if x[i][j]:
                    temp = x[i][j]
                    x[i][j] = 0
                    if x[target][j] == 0:
                        x[target][j] = temp
                    elif x[target][j] == temp:
                        x[target][j] *= 2
                        target += 1
                    else:
                        target += 1
                        x[target][j] = temp
    elif d == 3:  # 아래쪽
        for j in range(N):
            target = N-1
            for i in range(N-2, -1, -1):
                if x[i][j]:
                    temp = x[i][j]
                    x[i][j] = 0
                    if x[target][j] == 0:
                        x[target][j] = temp
                    elif x[target][j] == temp:
                        x[target][j] *= 2
                        target -= 1
                    else:
                        target -= 1
                        x[target][j] = temp
    return x


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
stack = [(deepcopy(arr), 0)]
while stack:
    x, cnt = stack.pop()
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                ans = max(ans, x[i][j])
        continue
    for i in range(4):
        temp_arr = move(deepcopy(x), i)
        stack.append((temp_arr, cnt + 1))
print(ans)
