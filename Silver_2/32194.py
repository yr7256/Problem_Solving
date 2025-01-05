import sys
input = sys.stdin.readline
N = int(input())
arr = [1]  # n번째 질문이 Yes인가 No인가
pre = [0, 1]  # 그에 대한 누적합 ex) pre[x]는 pre[0:x]의 누적합
for i in range(N):
    q, x, y = map(int, input().split())
    # q가 1일 때, x 질문부터 y 질문까지 다 1이어야 Yes, 아니면 No
    # 즉, pre[y]-pre[x-1]이 y-x+1 보다 작으면 이 구간 내에 0이 있다는 소리
    # q가 2일 때, x 질문부터 y 질문까지 다 0이어야 Yes, 아니면 No
    # 즉, pre[y]-pre[x-1]이 0보다 크면 이 구간 내에 1이 있다는 소리
    temp = pre[y]-pre[x-1]
    if q == 1:
        if temp < y-x+1:
            print('No')
            arr.append(0)
        else:
            print('Yes')
            arr.append(1)
    else:
        if temp > 0:
            print('No')
            arr.append(0)
        else:
            print('Yes')
            arr.append(1)
    pre.append(pre[-1]+arr[-1])
