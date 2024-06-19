# 1 2 3 4 5 6 7 8 9 10
# 1 1 1 1 1 1 1 1 1 1
#   1   1   1   1   1
#       2       2
#               4
# 1 3 4 8 9 11 12 20 21 23
# F(n) : f(1)~F(n) 까지의 합
# F(1) = 1
# F(2) = 2 + 1*1
# F(3) = 3 + 1*1
# F(4) = 4 + 2*1 + 1*2
# ...
# F(10) = 10 + 5*1 + 2*2 + 1*4
def sol(x):
    temp = 1
    ans = x
    while 2 ** temp <= x:
        ans += (x//(2**temp))*(2**(temp-1))
        temp += 1
    return ans


A, B = map(int, input().split())
print(sol(B)-sol(A-1))
