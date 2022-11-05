N = int(input())
students = [list(map(int, input().split())) for _ in range(N)]
students.sort(key=lambda x: -x[2])
print(*students[0][:2])
print(*students[1][:2])
if students[0][0] == students[1][0]:
    for i in students:
        if i[0] != students[0][0]:
            print(*i[:2])
            break
else:
    print(*students[2][:2])
