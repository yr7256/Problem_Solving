A, B = map(int, input().split())
max_val = max(A, B)
min_val = min(A, B)
print(((A+B)*(max_val-min_val+1))//2)
