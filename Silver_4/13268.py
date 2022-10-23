N = int(input())
N = N % 100
if N == 10 or N == 30 or N == 60 or N == 0:
    print(0)
elif 0 < N <= 15 or 25 <= N <= 35 or 55 <= N <= 65 or 95 <= N < 100:
    print(1)
elif 15 < N < 25 or 35 < N <= 40 or 50 <= N < 55 or 65 < N <= 70 or 90 <= N < 95:
    print(2)
elif 40 < N < 50 or 70 < N <= 75 or 85 <= N < 90:
    print(3)
elif 75 < N < 85:
    print(4)
