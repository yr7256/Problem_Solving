# N = int(input())
# cards = list(map(int, input().split()))
# for i in range(N):
#     cards[i] = (i+1, cards[i]/(i+1))
# cards.sort(key=lambda x: x[1], reverse=True)
# price = 0
# for i in cards:
#     if i[0] <= N:
#         div = N//i[0]
#         N -= i[0]*div
#         price += i[0]*i[1]*div
# print(int(price))
'''
틀렸다. 생각해보니 1장당 비율로 사면 분명히 안되는 경우가 있다.
반례) 5장 샀을때 1 50 70 1 1 이라면 2장+3장 샀을때 가장 비싸다.
그렇기에 그리디보다는 dp로 접근하는 것이 맞는거 같다.
'''
N = int(input())
cards = [0]+list(map(int, input().split()))
dp = [0]*(N+1)
for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j]+cards[j])
print(dp[N])
