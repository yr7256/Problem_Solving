arr = [input() for _ in range(3)]
ans = 0
for i in range(3):
    if arr[i].isdigit():
        ans = int(arr[i])+(3-i)
        break
if not ans % 15:
    print('FizzBuzz')
elif not ans % 3:
    print('Fizz')
elif not ans % 5:
    print('Buzz')
else:
    print(ans)
