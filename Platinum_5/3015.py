'''
500000 이므로 O(N^2) 안됨
조건 : 두 사람 A와 B가 서로 볼 수 있으려면, 두 사람 사이에 A 또는 B보다 키가 큰 사람이 없어야 한다.
A, B 가 있다고 가정
A>B 면 B 뒤에 B보다 크거나 같은 사람이 오더라도 볼 수 있다.
A=B 면 B 뒤에 B보다 크거나 같은 사람이 오더라도 볼 수 있다.
A<B 면 B 뒤에 누가 오더라도 볼 수 없다.
stack에 넣을 때 앞에 같은 키 같은 사람 몇 명인지 체크해야 함.
(키, 키 같은 사람 수)
스택을 감소하는 형태로 만들기.
만약 현재와 stack 맨 위에 있는 원소를 비교했을 때, 전자가 더 크다면 어차피 뒤에 들어오는 원소들도 후자를 보지 못한다.
이런 경우 stack pop 해주면서 ans 1 증가
같은 경우 중복 카운팅 변수 만들었으니 이 개수만큼 ans에 더해주면 된다.
ex) 1 1 1 1 이라면 처음에 stack에 [1, 1] append.
두번째 1 넣을때는  ans += 1, stack에서 pop() stack에 [1, 2] append
ans += 2, stack [1, 3] append. ans += 3, stack [1, 4] append. 반복되는 형태로 구성된다.
'''
import sys
input = sys.stdin.readline
N = int(input())
stack = []
ans = 0
for i in range(N):
    target = int(input())
    cnt = 1
    while stack and stack[-1][0] <= target:  # 스택을 감소하는 형태로 만들기
        if stack[-1][0] == target:
            ans += stack[-1][1]
            cnt = stack[-1][1]+1
            stack.pop()
        else:  # stack[-1][0] < target
            ans += stack[-1][1]
            stack.pop()
            cnt = 1
    if stack:
        ans += 1
    stack.append((target, cnt))
print(ans)
