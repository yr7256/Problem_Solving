import sys


def isprime(n):
    nums = [i for i in range(n+1)]
    for i in range(2, int(n**0.5)+1):
        if nums[i] == i:
            for j in range(i*i, n+1, i):
                if nums[j] == j:
                    nums[j] = i
    return nums


input = sys.stdin.readline
N = int(input())
plist = isprime(5000000)
for num in map(int, input().split()):
    ans = []
    while plist[num] > 1:
        ans.append(plist[num])
        num //= plist[num]
    print(*ans)
