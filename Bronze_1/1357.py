X, Y = map(str, input().split())
print(int(str(int(X[::-1])+int(Y[::-1]))[::-1]))
