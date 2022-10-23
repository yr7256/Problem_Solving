people_list = []
people = 0
for i in range(4):
    end, start = map(int, input().split())
    people += (start-end)
    people_list.append(people)
print(max(people_list))
