# from math import ceil
# while True:
#     N = int(input())
#     if N == 0:
#         break
#     else:
#         A = list(input().replace(' ', '').upper())
#         # while True:
#         #     A.append('x')
#         #     if len(A) % N == 0:
#         #         break
#         M = ceil(len(A) / N)
#         A_list = [A[i:i + M] for i in range(0, len(A), M)]
#         result = ''
#         for i in range(M):
#             for j in range(N):
#                 result += A_list[j][i]
#         result = result.replace('x', '')
#         print(result)

while True:
    N = int(input())
    if N == 0:
        break
    else:
        M = input().replace(" ", "").upper()
        result = [""] * len(M)
        q = len(M) // N
        r = len(M) % N
        a = 0
        for i in range(N):
            b = a + q
            if r:
                b += 1
                r -= 1
            result[i::N] = M[a:b]
            a = b
        print(*result, sep="")
