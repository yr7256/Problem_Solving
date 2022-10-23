V = int(input())
a, b = 0, 0
S = input()
for i in S:
    if i == 'A':
        a += 1
    else:
        b += 1
if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print('Tie')
