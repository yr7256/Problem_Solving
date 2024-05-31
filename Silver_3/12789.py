N = int(input())
students = list(map(int, input().split()))
curr = 1
stack = []
for student in students:
    stack.append(student)
    while stack and stack[-1] == curr:
        stack.pop()
        curr += 1
print('Sad' if stack else 'Nice')
