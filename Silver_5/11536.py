N = int(input())
name = [input() for _ in range(N)]
if name == sorted(name):
    print('INCREASING')
elif name == sorted(name)[::-1]:
    print('DECREASING')
else:
    print('NEITHER')
