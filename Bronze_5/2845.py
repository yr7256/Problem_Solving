L, P = map(int, input().split())
print(*[int(i)-(L*P) for i in input().split()])
