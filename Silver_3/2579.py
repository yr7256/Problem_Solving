import sys
input = sys.stdin.readline
N = int(input())
s = [0]*(301)
sum = [0]*(301)
for i in range(N):
    s[i] = int(input())
sum[0] = s[0]
sum[1] = s[0]+s[1]
sum[2] = max(s[0]+s[2], s[1]+s[2])
for j in range(3, N):
    sum[j] = max(sum[j-3]+s[j-1]+s[j], sum[j-2]+s[j])
print(sum[N-1])
