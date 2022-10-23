import sys
input = sys.stdin.readline
n = int(input())
profile = []
for i in range(n):
    student = input().split()
    student[1:] = map(int, student[1:])
    profile.append(student)
profile.sort(key=lambda x: (x[3], x[2], x[1]))
print(profile[-1][0])
print(profile[0][0])
