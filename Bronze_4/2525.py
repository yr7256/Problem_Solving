h, m = map(int, input().split())
m1 = int(input())
print((h+((m+m1)//60)) % 24, (m+m1) % 60)
