def back(x, y, count):
    global ans
    if x >= 10:
        ans = min(ans, count)
        return
    if y >= 10:
        back(x+1, 0, count)
        return
    if arr[x][y]:
        for l in range(1, 6):
            if paper[l] >= 5:
                continue
            if 0 <= x+l-1 < 10 and 0 <= y+l-1 < 10:
                flag = True
                for i in range(x, x+l):
                    for j in range(y, y+l):
                        if not arr[i][j]:
                            flag = False
                            break
                    if not flag:
                        break
                if flag:
                    for i in range(x, x+l):
                        for j in range(y, y+l):
                            arr[i][j] = 0
                    paper[l] += 1
                    back(x, y+l, count+1)
                    paper[l] -= 1
                    for i in range(x, x+l):
                        for j in range(y, y+l):
                            arr[i][j] = 1
    else:
        back(x, y+1, count)


arr = [list(map(int, input().split())) for _ in range(10)]
ans = 100
paper = [0]*6
back(0, 0, 0)
if ans == 100:
    print(-1)
else:
    print(ans)
'''
종이 저장할 리스트 만들기
큰거부터 넣는건 어떨까 - 고려해보자 (이 방법이 더 느리다)
1~5사이 넣고 되는지 안되는지 해보기
박스확인해서 안되면 flag=False 걸고 break
'''