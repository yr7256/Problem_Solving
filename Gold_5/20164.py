'''
odd_count 함수는 말 그대로 홀수 세는 함수.
minmax 함수는 1일때 2일때 3보다 크거나 같을 때 case 나눠서 생각하기!
1이나 2일때는 단순하다. 그냥 볼 case가 하나뿐이기 때문에 나눠서 연산해주면 됨.
3일때는 임의의 위치에서 잘라서 min,max를 갱신!
'''
def odd_count(n):
    count = 0
    while n:
        if (n % 10) % 2:
            count += 1
        n //= 10
    return count


def minmax(N, ans):
    global min_num, max_num
    ans += odd_count(int(N))
    if len(N) == 1:
        min_num = min(min_num, ans)
        max_num = max(max_num, ans)
        return
    elif len(N) == 2:
        num = int(N[0])+int(N[1])
        minmax(str(num), ans)
    else:
        for i in range(1, len(N)):
            for j in range(i+1, len(N)):
                left = int(N[:i])
                center = int(N[i:j])
                right = int(N[j:])
                num = left + center + right
                minmax(str(num), ans)


min_num, max_num = 100, 0
N = input()
minmax(N, 0)
print(min_num, max_num)
