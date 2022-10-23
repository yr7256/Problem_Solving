n, m = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
print(n+m-2*len(A & B))
