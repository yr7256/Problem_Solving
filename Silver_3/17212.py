'''
dp를 우선 엄청 큰 수로 두고 갱신하는 방법을 쓰자
배낭처럼 접근해보자
그냥 그리디처럼 풀면 반례가 생긴다
ex) 10일 때, 사실 최소값은 5*2로 2개지만 7부터 시작하면 7, 2, 1 이렇게 3개로 나오기 때문. 
'''
N = int(input())
dp = [100001]*(N+1)
dp[0] = 0
coins = [7, 5, 2, 1]
for i in range(1, N+1):
    for coin in coins:
        if coin <= i and dp[i-coin] < dp[i]:
            dp[i] = dp[i-coin]+1
print(dp[-1])
