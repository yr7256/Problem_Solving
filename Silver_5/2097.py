def solve(n):
    if n == 1 or n == 2:
        return 4
    else:
        root = round((n)**0.5)
        if root*root >= n:
            return (root-1)*4
        else:
            return ((root-1)*2)+(root*2)


N = int(input())
print(solve(N))
