def check(a):
    global ans
    for i in a:
        flag = True
        count = 1
        for j in range(1, N):
            if i[j] == i[j-1]:
                count += 1
            elif i[j] - i[j-1] == 1 and count >= L:     # 되면 count 초기화해주기
                count = 1
            elif i[j] - i[j-1] == -1 and count >= 0:    # 이부분 제일 어려웠다 (반대는 어떻게 쌓아줄까)
                count = -L+1                            # 빚을 청산해야 다음 단계로 갈 수 있다
            else:
                flag = False
                break
        if flag and count >= 0:
            ans += 1
N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
zipped_arr = list(map(list, zip(*arr)))
ans = 0
check(arr)
check(zipped_arr)
print(ans)