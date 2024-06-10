import sys
input = sys.stdin.readline
temp = 0
arr = [1]*1000001
arr[1] = 0

for i in range(2, 1414):
    temp += i-1
    for j in range(2, (1000000-temp)//i+1):
        arr[i*j+temp] += 1

while True:
    N = int(input())
    if N:
        print(arr[N])
    else:
        break
