'''
숫자야구는 중복숫자 하면 안되니까 일단 123에서 987까지 보자.
그 중에 중복되는 숫자랑 0 있는거 일단 제거시켜주고 시작하기.
브루트포스 돌려서 조건에 만족하는거 True 해주고 아닌건 False
다른 것도 다 돌려보면 조건에 만족하는 애들만 남는다.
'''
import sys
input = sys.stdin.readline
num_list = [True]*1000
N = int(input())
for _ in range(N):
    num, s, b = map(int, input().split())
    num = str(num)
    for i in range(123, 988):
        si = str(i)
        if si[0] == si[1] or si[1] == si[2] or si[2] == si[0]:
            num_list[i] = False
        if si[0] == '0' or si[1] == '0' or si[2] == '0':
            num_list[i] = False
        s_count = 0
        b_count = 0
        for j in range(3):
            for k in range(3):
                if si[j] == num[k]:
                    if j == k:
                        s_count += 1
                    else:
                        b_count += 1
        if num_list[i] and s_count == s and b_count == b:
            num_list[i] = True
        else:
            num_list[i] = False
count = 0
for i in range(123, 988):
    if num_list[i]:
        count += 1
print(count)
