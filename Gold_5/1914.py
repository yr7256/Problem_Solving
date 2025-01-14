'''
321 0 0
32 0 1
3 2 1
3 21 0 -> 맨 아래 제외한 원판 s, e 아닌 곳으로
0 21 3 -> 원판 옮기면서 s->s,e 아닌 곳으로 바뀌면서 새로 시작됨
1 2 3
1 0 32
0 0 321
'''


def hanoi(n, s, e):
    if n == 1:
        print(s, e)
        return
    hanoi(n-1, s, 6-s-e)
    print(s, e)
    hanoi(n-1, 6-s-e, e)


N = int(input())
print(2**N-1)
if N <= 20:
    hanoi(N, 1, 3)
