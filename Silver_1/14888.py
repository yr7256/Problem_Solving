import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
oper = list(map(int, input().split()))
maximum = -sys.maxsize
minimum = sys.maxsize


def solution(num, answer, pl, mi, multi, div):
    global maximum, minimum
    if num == N:
        maximum = max(maximum, answer)
        minimum = min(minimum, answer)
        return
    if pl:
        solution(num+1, answer+A[num], pl-1, mi, multi, div)
    if mi:
        solution(num+1, answer-A[num], pl, mi-1, multi, div)
    if multi:
        solution(num+1, answer*A[num], pl, mi, multi-1, div)
    if div:
        solution(num+1, int(answer/A[num]), pl, mi, multi, div-1)


solution(1, A[0], oper[0], oper[1], oper[2], oper[3])
print(maximum)
print(minimum)
