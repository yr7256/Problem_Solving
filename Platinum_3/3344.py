N = int(input())
even_list = [i for i in range(2, N+1, 2)]
odd_list = [i for i in range(1, N+1, 2)]
if N % 6 == 2 or N % 6 == 3:
    if N % 6 == 2:
        odd_list[0], odd_list[1] = odd_list[1], odd_list[0]
        odd_list.pop(2)
        odd_list.append(5)
    else:
        even_list.append(even_list.pop(0))
        odd_list.append(odd_list.pop(0))
        odd_list.append(odd_list.pop(0))
    for i in (*even_list, *odd_list):
        print(i)
else:
    for i in (*odd_list, *even_list):
        print(i)
