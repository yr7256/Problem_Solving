'''
itertools는 신이다
주어진 숫자에서 6개 뽑아서 조합 돌리자
'''
from itertools import combinations
while True:
    case = list(map(int, input().split()))
    num = case[0]
    lotto = case[1:]
    lotto_list = list(combinations(lotto, 6))
    for i in lotto_list:
        print(*i)
    if num == 0:
        break
    print()
