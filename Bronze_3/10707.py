A, B, C, D, P = [int(input()) for _ in range(5)]
X = A*P
if C < P:
    Y = B+((P-C)*D)
else:
    Y = B
print(min(X, Y))
