N = input()
i = 0
result = 0
while i < len(N)-1:
    result += 9*(10**i)*(i+1)
    i += 1
result += (int(N)-(10**(len(N)-1))+1)*len(N)
print(result)
