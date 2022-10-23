import math
A, B, V = map(int, input().split())
D = (V-B)/(A-B)
print(math.ceil(D))
