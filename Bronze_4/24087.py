from math import ceil
S = int(input())
A = int(input())
B = int(input())
X = (S-A)/B
print(250+100*ceil(X) if X > 0 else 250)
