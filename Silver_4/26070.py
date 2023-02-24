A, B, C = map(int, input().split())
X, Y, Z = map(int, input().split())
ans = 0
for i in range(3):
    chicken = min(A, X)
    ans += chicken
    A -= chicken
    X -= chicken
    pizza = min(B, Y)
    ans += pizza
    B -= pizza
    Y -= pizza
    burger = min(C, Z)
    ans += burger
    C -= burger
    Z -= burger
    X, Y, Z = X % 3 + Z//3, Y % 3 + X//3, Z % 3 + Y//3
print(ans)