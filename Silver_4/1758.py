N = int(input())
tip = [int(input()) for _ in range(N)]
ans = 0
# tip.sort(reverse=True)
# for i in range(N):
#     if tip[i]-i > 0:
#         ans += tip[i]-i
# print(ans)

for i, t in enumerate(sorted(tip, reverse=True)):
    ans += max(t-i, 0)
print(ans)

# 거꾸로 정렬해서 index만큼 빼주면 된다. -> enumerate
