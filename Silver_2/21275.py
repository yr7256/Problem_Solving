# int(string, 진법) : string을 10진법으로 바꿔줌
A, B = input().split()
X, num_A, num_B = 0, 0, 0                           # 10진법으로 바꾼수, A진법, B진법
count = 0                                           # 경우의 수 저장
for i in range(2, 37):                              # 36진법까지니까 range(2,37)
    for j in range(2, 37):                          #
        try:                                        # 진법변환 되는거만 할 수 있게 try except 쓰자
            if i == j:                              # 문제 조건에서 num_A != num_B 이므로 지나가기
                continue                            #
            if int(A, i) == int(B, j):              # 진법변환 했을 때 같으면 수 저장하기
                X, num_A, num_B = int(A, i), i, j   #
                count += 1                          #
        except ValueError:                          #
            continue                                #
if X < 2**63:                                       #
    if count == 0:                                  #
        print('Impossible')                         #
    elif count == 1:                                #
        print(X, num_A, num_B)                      #
    else:                                           #
        print('Multiple')                           #
else:                                               #
    print('Impossible')                             #
