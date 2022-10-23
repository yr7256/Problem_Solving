A, B, C = map(int, input().split())
a = min(A, B, C)
if A+B+C < 100:
    if a == A:
        print('Soongsil')
    if a == B:
        print('Korea')
    if a == C:
        print('Hanyang')
else:
    print('OK')
