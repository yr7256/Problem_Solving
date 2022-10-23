'''
출석 결석한 사람들 리스트에 넣어서 체크해준다
그 다음에 출석 못한 사람들 걍 빼주기 (1-attend[i] 가 1이면 결석이고 0이면 출석이라는 소리) 
'''
import sys
input = sys.stdin.readline
N, K, Q, M = map(int, input().split())
K_list = list(map(int, input().split()))
Q_list = list(map(int, input().split()))
absent = [0]*(N+3)
attend = [0]*(N+3)
ans = [0]*(N+3)
for i in K_list:
    absent[i] = 1
for i in Q_list:
    if absent[i]:
        continue
    for j in range(i, N+3, i):
        if not absent[j]:
            attend[j] = 1
for i in range(3, N+3):
    ans[i] = 1-attend[i]+ans[i-1]
for _ in range(M):
    start, end = map(int, input().split())
    print(ans[end]-ans[start-1])
