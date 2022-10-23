A, B = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
if a-b:
    print(len(a-b))
    print(*sorted(a-b))
else:
    print(0)
