def stars(n):
    if n == 1:
        return['*']
    star_partition = stars(n//3)
    temp = []
    for i in star_partition:
        temp.append(i*3)
    for i in star_partition:
        temp.append(i+' '*(n//3)+i)
    for i in star_partition:
        temp.append(i*3)
    return temp


N = int(input())
print(*stars(N), sep='\n')
