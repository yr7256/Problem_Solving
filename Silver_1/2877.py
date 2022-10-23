N = int(input())
ans = bin(N+1)[3:]
print(ans.replace('0', '4').replace('1', '7'))
