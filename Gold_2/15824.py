'''
O(N^2)으로는 안됨
(각 조합에서 최댓값)-(각 조합에서 최솟값)
ex) [2, 5, 8] 일 때 가능한 경우는 2 5 8 25 28 58 258 인데
여기서 값을 구해보면 (2-2)+(5-5)+(8-8)+(5-2)+(8-2)+(8-5)+(8-2)
=2*(1-4)+5*(2-2)+8*(4-1)
즉, arr을 sort한 뒤 arr[i]*(2^i-2^(N-i-1)) 값을 0에서 N-1까지 더해주면 된다.
파이썬 pow 함수 사용할 경우, 큰 수 대응 x
분할 정복으로 풀어야함.
'''


def half(n, k):
    if k == 0:
        return 1
    if k == 1:
        return n
    if k % 2:
        return (half(n, k//2)**2*n) % num
    else:
        return (half(n, k//2)**2) % num


N = int(input())
num = 1000000007
arr = list(map(int, input().split()))
arr.sort()
ans = 0
for i in range(N):
    ans += arr[i]*(half(2, i)-half(2, N-i-1))
print(ans % num)
