from math import factorial
C = int(input())
for _ in range(C):
    testcase = input().split()
    testcase[1:] = map(int, testcase[1:])
    S, N, T, L = testcase[0], testcase[1], testcase[2], testcase[3]
    if S == 'O(N)':
        if N*T <= L*100000000:
            print('May Pass.')
        else:
            print('TLE!')
    elif S == 'O(N^2)':
        if (N**2)*T <= L*100000000:
            print('May Pass.')
        else:
            print('TLE!')
    elif S == 'O(N^3)':
        if (N**3)*T <= L*100000000:
            print('May Pass.')
        else:
            print('TLE!')
    elif S == 'O(2^N)':
        if (2**N)*T <= L*100000000:
            print('May Pass.')
        else:
            print('TLE!')
    elif S == 'O(N!)':
        if factorial(N)*T <= L*100000000:
            print('May Pass.')
        else:
            print('TLE!')
