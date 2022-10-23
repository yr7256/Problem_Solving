from itertools import combinations
N = int(input())
decrease = []
for i in range(1, 11):
    for num in combinations(range(10), i):
        num = list(num)
        num.sort(reverse=True)
        decrease.append(int(''.join(map(str, num))))
decrease.sort()
try:
    print(decrease[N])
except:
    print(-1)
