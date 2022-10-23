# RecursionError
# def back(start, answer):
#     global count
#     if start > n:
#         return
#     if n == start:
#         if answer == answer[::-1]:
#             count += 1
#     else:
#         for i in range(1, 4):   # 1, 2, 3 만 더한다. (문제 조건)
#             back(start+i, answer+str(i))


# T = int(input())
# for _ in range(T):
#     n = int(input())
#     count = 0
#     back(0, '')
#     print(count % 1000000009)

dp = [1, 1, 2, 2, 3, 3]
for i in range(6, 100001):
    dp.append(dp[i-2]+dp[i-4]+dp[i-6])
T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n] % 1000000009)
