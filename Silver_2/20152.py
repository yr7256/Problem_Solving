from math import comb
H, N = map(int, input().split())
x = abs(H-N)
print(comb(2*x, x)//(x+1))
